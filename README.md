# FastAPI / uv / Data Science

<p align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI">
</p>
<p align="center">
  <img src="https://docs.astral.sh/uv/assets/logo-letter.svg" alt="UV">
</p>
<p align="center">
  <img src="https://img.favpng.com/16/15/2/data-science-machine-learning-data-analysis-png-favpng-KNXS0CX59QEHyqU2kqV7aL3pq.jpg" alt="Data Science">
</p>



<p align="left">
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>

</p>

---

## Creating a virtual environment

```bash
# uv supports creating virtual environments, e.g., to create a virtual environment at .venv:
$ uv venv
```

## Using a virtual environment

```bash
# When using the default virtual environment name, uv will automatically find and use the virtual environment during subsequent invocations.
$ uv venv

# Install a package in the new virtual environment
$ uv pip install ruff

# The virtual environment can be "activated" to make its packages available:

# Linux
$ source .venv/bin/activate

#windows
.venv\Scripts\activate

# Deactivating an environment
$ deactivate

```

## Creating a new project (Ex - project name: fastapi)

```bash
# You can create a new Python project using the uv init command:

$ uv init fastapi
$ cd fastapi

# Alternatively, you can initialize a project in the working directory:

$ mkdir fastapi
$ cd fastapi
$ uv init

# uv will create the following files:
.
├── .python-version
├── README.md
├── main.py
└── pyproject.toml

# The main.py file contains a simple "Hello world" program. Try it out with uv run:

$ uv run main.py
```

## pyproject.toml
```bash
The pyproject.toml contains metadata about your project:

pyproject.toml

[project]
name = "fastapi"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
dependencies = []
```

## For example, to use flask:
```bash
$ uv add flask
$ uv run -- flask run -p 3000
```

## Or, to run a script:
```python
# Require a project dependency
import flask

print("hello world")
```
```bash
$ uv run example.py
```
### Alternatively, you can use uv sync to manually update the environment then activate it before executing a command:

### Linux
```bash
$ uv sync
$ source .venv/bin/activate
$ flask run -p 3000
$ python example.py
```

### Windows
```bash
uv sync
source .venv\Scripts\activate
$ flask run -p 3000
$ python example.py
```

### Building distributions
uv build can be used to build source distributions and binary distributions (wheel) for your project.

By default, uv build will build the project in the current directory, and place the built artifacts in a dist/ subdirectory:

```bash
uv build
ls dist/
```
See the documentation on building projects for more details (https://docs.astral.sh/uv/concepts/projects/build/).