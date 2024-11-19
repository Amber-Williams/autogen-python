from projen.python import (PythonProject, PoetryPyprojectOptionsWithoutDeps, PythonSample)
from projen import TextFile

python_module_name = "src"
python_version = "3.12"

poetry_options = PoetryPyprojectOptionsWithoutDeps(
    packages=[
        {"include": python_module_name},
        {"include": "tests"},
        {"include": "utils"},
    ],
    scripts={
        "start": "scripts:start",
        "test": "scripts:test",
        "lint": "scripts:lint",
        "format": "scripts:format",
    },
    python_version=python_version,
)

project = PythonProject(
    author_email="https://github.com/Amber-Williams",
    author_name="amber williams",
    module_name=python_module_name,
    name="project_name",
    description="A project description",
    license="MIT",
    version="0.1.0",
    poetry=True,
    poetry_options=poetry_options,
    pytest=True,
    deps=["nanodjango"],
    dev_deps=["pytest-django", "ruff"],
)


MAKEFILE_CONTENTS = """\
SHELL = /bin/bash
.SHELLFLAGS = -o pipefail -c

.PHONY: install
install: ## installs dependencies
	poetry install

.PHONY: start
start: ## starts the app
	poetry run start

.PHONY: test
test: ## runs tests
	poetry run test

.PHONY: dustoff
dustoff: ## formats and verifies code
	poetry run format && poetry run lint

"""

MAKEFILE = TextFile(
    project,
    "Makefile",
    lines=MAKEFILE_CONTENTS.splitlines(),
    committed=True,
    readonly=True,
)

README = """\
This is a sample README.md for a Python project.

npx projen new python --poetry=true --python_module_name=src --name=project_name
npx projen --watch
npx projen eject
"""

README = TextFile(
    project,
    "README.md",
    lines=README.splitlines(),
    committed=True,
    readonly=True
)

SCRIPTS_FILE = """\
from subprocess import check_call

def start() -> None:
    check_call(["python", "-m", "src"])

def test() -> None:
    check_call(["pytest", "tests"])

def lint() -> None:
    check_call(["ruff", "check"])

def format() -> None:
    check_call(["ruff", "format"])
"""

SCRIPTS_FILE = TextFile(
    project,
    "scripts.py",
    lines=SCRIPTS_FILE.splitlines(),
    committed=True,
    readonly=True
)

PythonSample(project, dir="utils")

project.synth()