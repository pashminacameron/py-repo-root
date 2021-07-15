# Introduction 

This package standardizes the handling of paths in a Python project by 
allowing all paths to be relative to the project repo root. 
The package discovers the project root 
based on the location of a special (empty) `.py-repo-root` file. The project root can also be inferred based on the presence of any of the commonly used project root indicator files such as 
- .py-repo-root (empty file)
- .git
- .here (empty file)
- requirements.txt
- environment.yml
- .flake8
- setup.py
- pyproject.toml
 
This package was heavily inspired by [pyprojroot](https://github.com/chendaniely/pyprojroot). 
This package allows custom root file indicators, avoids recursive "/" is parent of "/" issue and can use 
the current file location to start walking the directory tree.

## Usage

Installation:
```
pip install py-repo-root
```

## Usage

Get project root, using the default list of project root indicators
```
from pathlib import Path
from pyreporoot import project_root

project_root_dir = project_root(Path(__file__))
```

Specify a custom project root indicator (not included in the list above)

```
project_root_dir = project_root(Path(__file__), root_files='.my-root-indicator')
```

Another common usage pattern may be to add the project_root to PYTHONPATH for the purposes 
of running some scripts. 

```
import sys
from pathlib import Path
from pyreporoot import project_root

sys.path.insert(0, str(project_root(Path(__file__), root_files='requirements.txt')))
```
Getting a relative path from the project root for a file:

```
from pathlib import Path
from projectroot import project_root

path_to_file_from_project_root = project_root(Path(__file__), root_files='requirements.txt').joinpath('/path/to/file.txt')
```



