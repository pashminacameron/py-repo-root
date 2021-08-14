from pyreporoot import project_root
from pathlib import Path

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
