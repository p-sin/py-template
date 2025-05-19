# py-template

Template for Python projects, including:

- uv configuaration
- pre-commit hooks
- nox (including github workflow)
- security github workflow


Instructions below are for setting up a VS code environment for the first time

1. Install python (interpreter) and uv (dependency manager)
    - Python: <https://www.python.org/downloads/>
    - uv: <https://github.com/astral-sh/uv>

2. VS code settings
    - Auto save on focus change
    - Black linting

3. Extensions
    - autopep8
    - Black Formatter
    - isort
    - Mypy
    - Pylance
    - Pylint
    - Python
    - Ruff

    - Even Better TOML
    - markdownlint
    - Jupyter
    - rainbow csv
    - parquet viewer
    - SQLite viewer

    - GitHub Pull Requests
    - GitLens - Git supercharged
    - GitHub Actions

    - autoDocstring
    - Error Lens
    - GitHub CoPilot

4. Set up python version (if needed)
    - <https://github.com/pyenv/pyenv>
    - pyenv install [version number]
    - pyenv local [version number]

5. uv (dependency manager)
    - Add depdendencies: `uv add` or `uv add --dev`
    - Remove dependencies: `uv remove`
    - Use `uv sync` to make/update virutal environment from poetry config
    - If does not create new virtual env, is because it is in one. Set to base python in select interpreter, then install again

6. Set up git repo
    - Create repo on github
    - Create local folder
    - `git init`
    - `git remote add origin [url]`
    - `git fetch`
    - `git checkout main`

7. Dev tools
    - Added as dependencies in pyproject.toml with Config added in pyproject.toml or separate files
    - Called by pre-commit, github workflow and nox
    - Tools:

        - Black (configured through ruff)
        - Ruff (configured in pyproject.toml)
        - Mypy (configured in pyproject.toml and .github/linters/.mypy.ini)
        - isort
        - coverage (configured in .coveragerc)
        - pre-commit (configured in pre-commit-config.yaml then run ```pre-commit install```)
        - Nox (configured in noxfile.py), includes:
            - ruff
            - black
            - isort
            - pytest
            - coverage
            - mypy
            - safety
            - checkov
            - trufflehog
        - pytest (configured in pyproject.toml)

8. GitHub workflows
    - Configured in .github/workflows

9. Useful libraries
    - Pydantic (model validation)
