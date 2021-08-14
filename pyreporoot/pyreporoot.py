"""
This file is heavily based on https://github.com/chendaniely/pyprojroot (MIT license)
but includes some additional fixes:

    1. "/" being parent of "/", leading to recursion error
    2. current working directory being used instead of invoking file path
    3. a custom root_files filter

"""

from pathlib import Path
from typing import Union, Iterable


def py_project_root(path: Path, project_files: Iterable) -> Path:
    """
    Recursively searches for project files in the current working directory
    to find the project root of the python project.
    :param path: pathlib path object
    :param project_files: list of to track project files
    :return: pathlib path
    """
    for file in project_files:
        found = list(path.glob(file))
        if len(found) > 0:
            return path
    if path.parent == path:
        raise FileNotFoundError("Project root directory not found.")
    else:
        return py_project_root(path.parent, project_files)


def project_root(
    file_path: str,
    root_files: Union[str, Iterable[str]] = (".py-repo-root"),
) -> str:
    # Get absolute path to avoid . is parent of . issue
    file_path = Path(file_path).resolve()
    if isinstance(root_files, str):
        root_files = (root_files,)
    project_path = py_project_root(path=file_path, project_files=root_files)
    if project_path.exists():
        return str(project_path)
    else:
        raise FileExistsError("Project root does not exist?")
