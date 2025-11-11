This file is a merged representation of the entire codebase, combined into a single document.
The content has been processed for AI analysis and code review purposes.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and default ignore patterns
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Repository Information
- **Repository URL:** https://github.com/Nirvisha82/devflow-test.git
- **Repository Name:** devflow-test
- **Total Files Analyzed:** 6
- **Generated:** 2025-10-23 11:59:56

# Directory Structure
```
.devflow/
  repo-structure.md
.gitignore
README.md
app.py
calculator/
  __init__.py
  calculator.py
  operations.py
```

# Files

## File: .gitignore
````
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[codz]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py.cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock
#poetry.toml

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#   pdm recommends including project-wide configuration in pdm.toml, but excluding .pdm-python.
#   https://pdm-project.org/en/latest/usage/project/#working-with-version-control
#pdm.lock
#pdm.toml
.pdm-python
.pdm-build/

# pixi
#   Similar to Pipfile.lock, it is generally recommended to include pixi.lock in version control.
#pixi.lock
#   Pixi creates a virtual environment in the .pixi directory, just like venv module creates one
#   in the .venv directory. It is recommended not to include this directory in version control.
.pixi

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.envrc
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

# Abstra
# Abstra is an AI-powered process automation framework.
# Ignore directories containing user credentials, local state, and settings.
# Learn more at https://abstra.io/docs
.abstra/

# Visual Studio Code
#  Visual Studio Code specific template is maintained in a separate VisualStudioCode.gitignore 
#  that can be found at https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore
#  and can be added to the global gitignore or merged into this file. However, if you prefer, 
#  you could uncomment the following to ignore the entire vscode folder
# .vscode/

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc

# Cursor
#  Cursor is an AI-powered code editor. `.cursorignore` specifies files/directories to
#  exclude from AI features like autocomplete and code analysis. Recommended for sensitive data
#  refer to https://docs.cursor.com/context/ignore-files
.cursorignore
.cursorindexingignore

# Marimo
marimo/_static/
marimo/_lsp/
__marimo__/
````

## File: README.md
````markdown
# devflow-test

Test Calculator app using python for DevFlow Agent.

The app supports following operations:
1) Addition
2) Substraction
````

## File: app.py
````python
from calculator import Calculator

def prompt_number(label: str) -> float:
    while True:
        try:
            return float(input(f"Enter {label} number: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main() -> None:
    calc = Calculator()

    print("Simple OOP Calculator (Add & Subtract)")
    print("======================================")

    while True:
        print("\nOptions:")
        for key, op in calc.menu_items.items():
            print(f"{key}. {op.name}")
        print("q. Exit")

        choice = input("Enter your choice: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            print("Exiting... Goodbye!")
            break

        if choice not in calc.menu_items:
            print("Invalid choice! Try again.")
            continue

        a = prompt_number("first")
        b = prompt_number("second")

        try:
            result = calc.compute(choice, a, b)
            op_name = calc.menu_items[choice].name
            symbol = "+" if op_name == "Add" else "-"
            print(f"Result: {a} {symbol} {b} = {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
````

## File: calculator/__init__.py
````python
from .calculator import Calculator
from .operations import Operation, Add, Subtract

__all__ = ["Calculator", "Operation", "Add", "Subtract"]
````

## File: calculator/calculator.py
````python
from typing import Dict, Type
from .operations import Operation, Add, Subtract

class Calculator:
    """
    Simple OOP calculator that delegates to Operation objects.
    You can register new operations without changing the UI.
    """
    def __init__(self) -> None:
        self._operations: Dict[str, Operation] = {}
        self._register_default_operations()

    def _register_default_operations(self) -> None:
        self.register_operation("1", Add())
        self.register_operation("2", Subtract())

    def register_operation(self, key: str, operation: Operation) -> None:
        self._operations[key] = operation

    @property
    def menu_items(self) -> Dict[str, Operation]:
        return self._operations

    def compute(self, key: str, a: float, b: float) -> float:
        if key not in self._operations:
            raise KeyError(f"Unknown operation key: {key}")
        return self._operations[key].execute(a, b)
````

## File: calculator/operations.py
````python
from abc import ABC, abstractmethod

class Operation(ABC):
    name: str

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        ...

class Add(Operation):
    name = "Add"

    def execute(self, a: float, b: float) -> float:
        return a + b

class Subtract(Operation):
    name = "Subtract"

    def execute(self, a: float, b: float) -> float:
        return a - b
````

