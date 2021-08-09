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
    file_path = Path(__file__).resolve()
    if isinstance(root_files, str):
        root_files = (root_files,)
    project_path = py_project_root(path=file_path, project_files=root_files)
    if project_path.exists():
        return str(project_path)
    else:
        raise FileExistsError("Project root does not exist?")


if __name__ == "__main__":
    # Specify where to start searching
    project_root_path = project_root(__file__)
    print(f"Project root: {project_root_path}")
    # Specify which files indicate repo root (you can choose your own root indicator file)
    # If the file is not present in the repo, FileNotFoundError is thrown
    custom_indicator = ["setup.py"]
    custom_project_path = project_root(__file__, root_files=custom_indicator)
    print(
        f"Project root with custom indicator {custom_indicator}: {custom_project_path}"
    )
    # To use a path relative to the project root, use joinpath
    print(
        f"File path from project root: {Path(project_root_path).joinpath('setup.py')}"
    )
