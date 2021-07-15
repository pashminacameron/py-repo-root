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
    file_path: Union[Path, str],
    root_files: Union[str, Iterable[str]] = (
        ".py-repo-root",
        ".git",
        ".here",
        "requirements.txt",
        "environment.yml",
        ".flake8",
        "setup.py",
        "pyproject.toml",
    ),
):
    if isinstance(file_path, str):
        file_path = Path(file_path)
    if isinstance(root_files, str):
        root_files = (root_files,)
    # Get absolute path to avoid . is parent of . issue
    file_path = file_path.resolve()
    project_path = py_project_root(path=file_path, project_files=root_files)
    if project_path.exists():
        return project_path
    else:
        raise FileExistsError("Project root does not exist?")


if __name__ == "__main__":
    # Specify where to start searching
    print(f"Project root: {project_root(Path(__file__))}")
    # Specify which files indicate repo root (you can choose your own root indicator file)
    # If the file is not present in the repo, FileNotFoundError is thrown
    print(f"Project root: {project_root(Path(__file__), root_files=['requirements.txt', '.here'])}")
    # To use a path relative to the project root, use joinpath
    print(
        f"File path from project root: {project_root(Path(__file__), root_files='requirements.txt').joinpath('setup.py')}"
    )
