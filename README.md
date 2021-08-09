# Introduction 

This package standardizes the handling of paths in a Python project by 
allowing all paths to be relative to the project repo root. 
The package discovers the project root 
based on the location of a special (empty) `.py-repo-root` file. 
The project root indicator can be overriden with a custom one, if desired.
 
This package was heavily inspired by [pyprojroot](https://github.com/chendaniely/pyprojroot). 
This package allows custom root file indicators, 
avoids recursive "/" is parent of "/" issue and can use 
the current file location to start walking the directory tree.

## Setup

Installation:
```
pip install py-repo-root
```

## Usage

Get project root, using the default list of project root indicators
```
from pyreporoot import project_root

project_root_dir = project_root(__file__)
```

Specify a custom project root indicator (not included in the list above)

```
project_root_dir = project_root(__file__, root_files='.my-root-indicator')
```

Another common usage pattern may be to add the project_root to PYTHONPATH for the purposes 
of running some scripts. 

```
import sys
from pyreporoot import project_root

sys.path.insert(0, project_root(__file__))
```
Getting a relative path from the project root for a file:

```
from pathlib import Path
from projectroot import project_root

project_root_dir = project_root(__file__)
path_rel_to_project_root = Path(project_root_dir).joinpath('/path/to/file.txt')
```



