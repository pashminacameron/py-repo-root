# Introduction 

This package standardizes the handling of paths in a Python project by 
allowing all paths to be relative to the project repo root. 
The package also helps discover the project root automatically 
based on the location of the file that invokes it and a user-specified
 (or commonly used) project root indicator files such as `requirements.txt`. 
 
This package was heavily inspired by [pyprojroot](https://github.com/chendaniely/pyprojroot). 
Our version allows custom root file indicators, avoids recursive "/" is parent of "/" issue and can use 
the current file location to start walking the directory tree.

## Usage

Installation:
```
pip install py-repo-root
```

## Usage

Get project root
```
from pathlib import Path
from pyreporoot import project_root

project_root_dir = project_root(Path(__file__), root_files='requirements.txt')
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



