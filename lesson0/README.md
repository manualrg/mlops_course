
# Objective
Set up a virtual environment to run project code

# Create a virtual environment in Ubuntu (or WSL2)
Create a Virtual Environment called .venv in project root folder
PYTHON_INTERPRETER=Path to Python installation, e.g. /usr/bin/python3.7
```
virtualenv -p  <PYTHON_INTERPRETER> .venv

```

Activate venv:
```
source .venv/bin/activate
deactivate
```

Check instalation:
```
.venv/bin/python --version
```

Install dependencies:
```
.venv/bin/pip install -r requirements.txt
```

# Install source code as a library in current Virtual Environment
In  folder `shared_code/` there is a package called `src/` that stores source code. The goal is to install it as a library in our venv so as to avoid import problems

The project structure is as follows:

+-- shared_code
|   +-- src
+-- .venv
+-- pyproject.toml
+-- setup.py
+-- setup.cfg

The files `pyproject.toml`, `setup.py`, `setup.cfg` are configuration files to perform this step

When venv is activated and configuration files are properly setup, install it in editable mode:
```bash
pip install -e .
```