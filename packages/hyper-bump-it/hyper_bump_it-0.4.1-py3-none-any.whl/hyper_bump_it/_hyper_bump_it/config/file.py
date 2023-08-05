import dataclasses
from collections.abc import Sequence
from pathlib import Path
from typing import Optional, Union, cast

import tomlkit
from pydantic import (
    BaseModel,
    Field,
    StrictBool,
    StrictStr,
    ValidationError,
    root_validator,
    validator,
)
from tomlkit import TOMLDocument
from tomlkit.exceptions import TOMLKitError

from ..compat import TypeAlias
from ..error import (
    ConfigurationFileNotFoundError,
    ConfigurationFileReadError,
    InvalidConfigurationError,
    SubTableNotExistError,
)
from ..planned_changes import PlannedChange
from ..version import Version
from .core import (
    DEFAULT_ALLOWED_INITIAL_BRANCHES,
    DEFAULT_BRANCH_ACTION,
    DEFAULT_BRANCH_FORMAT_PATTERN,
    DEFAULT_COMMIT_ACTION,
    DEFAULT_COMMIT_FORMAT_PATTERN,
    DEFAULT_REMOTE,
    DEFAULT_SEARCH_PATTERN,
    DEFAULT_TAG_ACTION,
    DEFAULT_TAG_FORMAT_PATTERN,
    HYPER_CONFIG_FILE_NAME,
    PYPROJECT_FILE_NAME,
    GitAction,
    validate_git_action_combination,
)

ROOT_TABLE_KEY = "hyper-bump-it"
PYPROJECT_SUB_TABLE_KEYS = ("tool", ROOT_TABLE_KEY)


class HyperBaseMode(BaseModel):
    class Config:
        extra = "forbid"
        min_anystr_length = 1
        allow_mutation = False


class GitActions(HyperBaseMode):
    commit: GitAction = DEFAULT_COMMIT_ACTION
    branch: GitAction = DEFAULT_BRANCH_ACTION
    tag: GitAction = DEFAULT_TAG_ACTION

    @root_validator(skip_on_failure=True)
    def _check_git_actions(
        cls,
        values: dict[str, GitAction],
    ) -> dict[str, GitAction]:
        validate_git_action_combination(**values)
        return values


class Git(HyperBaseMode):
    remote: StrictStr = DEFAULT_REMOTE
    commit_format_pattern: StrictStr = DEFAULT_COMMIT_FORMAT_PATTERN
    branch_format_pattern: StrictStr = DEFAULT_BRANCH_FORMAT_PATTERN
    tag_format_pattern: StrictStr = DEFAULT_TAG_FORMAT_PATTERN
    allowed_initial_branches: frozenset[str] = DEFAULT_ALLOWED_INITIAL_BRANCHES
    extend_allowed_initial_branches: frozenset[str] = frozenset()
    actions: GitActions = GitActions()


class File(HyperBaseMode):
    file_glob: StrictStr  # relative to project root directory
    keystone: StrictBool = False
    search_format_pattern: StrictStr = DEFAULT_SEARCH_PATTERN
    replace_format_pattern: Optional[StrictStr] = None


HyperConfigFileValues: TypeAlias = dict[
    str, Union[list[File], Optional[StrictStr], Git]
]


class ConfigFile(HyperBaseMode):
    files: list[File] = Field(..., min_items=1)
    current_version: Optional[Version] = None
    show_confirm_prompt: StrictBool = True
    git: Git = Git()

    @validator("current_version", pre=True)
    def _check_version(cls, value: Optional[object]) -> Optional[Version]:
        if value is None:
            return None
        if isinstance(value, Version):
            return dataclasses.replace(value)
        if isinstance(value, str):
            return Version.parse(value)
        raise TypeError(
            "Value must be a version or a string that can be parsed into a version"
        )

    @root_validator(skip_on_failure=True)
    def _check_keystone_files(
        cls,
        values: HyperConfigFileValues,
    ) -> HyperConfigFileValues:
        files = cast(list[File], values["files"])
        keystone_file_count = sum(1 for file in files if file.keystone)
        if keystone_file_count > 1:
            raise ValueError("Only one file is allowed to be a keystone file")
        current_version = values.get("current_version")
        if current_version is None:
            if keystone_file_count == 0:
                raise ValueError(
                    "current_version must be set if there is not a keystone file"
                )
        elif keystone_file_count != 0:
            raise ValueError(
                "Configuration can't specify the current_version while also having a keystone file"
            )
        return values

    @property
    def keystone_config(self) -> Optional[tuple[str, str]]:
        for file in self.files:
            if file.keystone:
                return file.file_glob, file.search_format_pattern
        return None


class ConfigVersionUpdater:
    def __init__(
        self,
        config_file: Path,
        project_root: Path,
        full_document: TOMLDocument,
        config_table: TOMLDocument,
        newline: Optional[str],
    ) -> None:
        """
        Initialize instance.

        :param config_file: File to write updated contents to.
        :param project_root: Directory to look for a configuration file.
        :param full_document: Config document to be written to file. Possibly including other
            values beyond what is used for this program.
        :param config_table: Config document with only the values used for this program.
        :param newline: New line character sequence for the file. `None` if no new line characters
            are found.
        """
        self._config_file = config_file
        self._project_root = project_root
        self._full_document = full_document
        self._config_table = config_table
        self._newline = newline

    def __call__(self, new_version: Version) -> PlannedChange:
        """
        Write the new version back to the configuration file.

        :param new_version: Version that should be stored in the configuration file.
        :return: Representation of the update to occur to the configuration file.
        """
        old_content = self._full_document_text
        self._config_table["current_version"] = str(new_version)
        new_content = self._full_document_text
        return PlannedChange(
            self._config_file,
            self._project_root,
            old_content=old_content,
            new_content=new_content,
            newline=self._newline,
        )

    @property
    def _full_document_text(self) -> str:
        return tomlkit.dumps(self._full_document)


ConfigReadResult: TypeAlias = tuple[ConfigFile, Optional[ConfigVersionUpdater]]


def read_config(config_file: Optional[Path], project_root: Path) -> ConfigReadResult:
    """
    Read the appropriate configuration file.

    If `config_file` is given, that will be used as the dedicated configuration file to read.
    If `config_file` is not given, look for a configuration file in the project root. First check
    for a dedicated configuration file. If that doesn't exist, try pyproject.toml.

    :param config_file: Hyper config file to read from.
    :param project_root: Directory to look for a configuration file.
    :return: Parsed configuration content and an object that can be used to update the version
        stored in the configuration file. If the configuration uses a keystone file, this second
        values will be `None`.
    :raises ConfigurationError: No file was found or there was some error in the file.
    """
    if config_file is not None:
        return read_hyper_config(config_file, project_root)

    hyper_config_file = project_root / HYPER_CONFIG_FILE_NAME
    if hyper_config_file.exists():
        return read_hyper_config(hyper_config_file, project_root)

    pyproject_config_file = project_root / PYPROJECT_FILE_NAME
    if pyproject_config_file.exists():
        return read_pyproject_config(pyproject_config_file, project_root)

    raise ConfigurationFileNotFoundError(project_root)


def read_pyproject_config(
    pyproject_file: Path,
    project_root: Path,
) -> ConfigReadResult:
    """
    Read configuration from pyproject file.

    :param pyproject_file: Path to the file to read.
    :param project_root: Directory to look for a configuration file.
    :return: Parsed configuration content and an object that can be used to update the version
        stored in the configuration file. If the configuration uses a keystone file, this second
        values will be `None`.
    :raises ConfigurationError: Some error exists in the configuration file.
    """
    return _read_config(pyproject_file, PYPROJECT_SUB_TABLE_KEYS, project_root)


def read_hyper_config(
    hyper_config_file: Path,
    project_root: Path,
) -> ConfigReadResult:
    """
    Read configuration from pyproject file.

    :param hyper_config_file: Path to the decided configuration file to read.
    :param project_root: Directory to look for a configuration file.
    :return: Parsed configuration content and an object that can be used to update the version
        stored in the configuration file. If the configuration uses a keystone file, this second
        values will be `None`.
    :raises ConfigurationError: Some error exists in the configuration file.
    """
    return _read_config(hyper_config_file, [ROOT_TABLE_KEY], project_root)


def _read_config(
    config_file: Path, sub_tables: Sequence[str], project_root: Path
) -> ConfigReadResult:
    try:
        file_data = config_file.read_bytes()
        full_document = tomlkit.parse(file_data.decode())
    except (OSError, TOMLKitError) as ex:
        raise ConfigurationFileReadError(config_file, ex) from ex
    config_table = full_document
    for key in sub_tables:
        config_table = cast(TOMLDocument, config_table.get(key))
        if config_table is None:
            raise SubTableNotExistError(config_file, PYPROJECT_SUB_TABLE_KEYS)

    try:
        # Unwrap TOML objects so that the rest of the application operates on native types.
        config = ConfigFile(**config_table.unwrap())
    except ValidationError as ex:
        raise InvalidConfigurationError(config_file, ex)

    if config.current_version is None:
        # uses keystone file & doesn't need to write back to pyproject file.
        return config, None
    return config, ConfigVersionUpdater(
        config_file=config_file,
        project_root=project_root,
        full_document=full_document,
        config_table=config_table,
        newline=PlannedChange.detect_line_ending(file_data),
    )
