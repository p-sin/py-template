# py-template

Python repository template

1. Install python and poetry
    - Python: https://www.python.org/downloads/
    - Poetry: https://python-poetry.org/docs/

2. VS code settings
    - Auto save on focus change
    - Black linting

3. Extensions
    - autopep8
    - Black Formatter
    - isort
    - Mypy
    - Prettier
    - Pylance
    - Pylint
    - Python
    - Ruff

    - Even Better TOML
    - markdownlint
    - Jupyter

    - GitHub Pull Requests
    - GitLens - Git supercharged

    - autoDocstring
    - Error Lens
    - GitHub CoPilot

4. Set up python version (if needed)
    - https://github.com/pyenv/pyenv
    - pyenv install [version number]
    - pyenv local [version number]
    - poetry install
    - poetry env use [version]

5. Poetry
    - Create empty project folder
    - ```poetry new [project-name]``` or ```poetry init``` for existing project
    - Add depdendencies: ```poetry add```
    - Remove dependencies: ```poetry remove```
    - Use ```poetry install``` to make/update virutal environment from poetry config
    - If does not create new virtual env, is because it is in one. Set to base python in select interpreter, then install again
    - dev-dependencies:
        - nox
        - pre-commit
        - black
        - isort
        - ruff
        - mypy
        - typing-extensions
        - pytest
        - pytest-cov
        - coverage

6. Set up git repo
    - Create repo on github
    - Create local folder
    - ```git init```
    - ```git remote add origin [url]```
    - Add .gitignore

7. pytest
    - ```poetry add pytest```
    - ```poetry add pytest-cov```
    - Add the following to pyproject.toml

        ``` toml

        [tool.pytest.ini_options]
        pythonpath = ["py_template"]
        addopts = "--cov=py_template"
        testpaths = ["tests/"]

        [tool.coverage.paths]
        source = ["py_template"]

        [tool.coverage.run]
        branch = true
        source = ["py_tepmplate"]
        ```

8. Ruff and mypy in pyroject

    ``` toml
    [tool.mypy]
    mypy_path = ["py_template"]
    strict = true
    namespace_packages = false

    [tool.ruff]
    lint.select = [
        "A",   # flake8-builtins (redefinition of bultins)
        "ANN", # flake8-annotations (type annotations are everywhere)
        "ARG", # flake8-unused-arguments (unused argument in function/method/class/lambda)
        "B",   # flake8-bugbear (bugs & design problems)
        "B9",  # flake8-bugbear strict (bugs & design problems)
        "BLE", # flake8-blind-except (no "except:" or "except Exception:")
        # "COM", # flake8-commas (force trailing commas) -> unelegant
        "C4",  # flake8-comprehensions (better list/set/dict comprehensions)
        "C90", # McCabe (code complexity)
        "D",   # pydocstyle (documentation style)
        "DJ",  # flake8-django (practices on Django)
        "DTZ", # flake8-datetimez (usage of unsafe naive datetime class)
        "E",   # pycodestyle (violation of PEP-8)
        "EM",  # flake8-errmsg (format error messages)
        "EXE", # flake8-executable (executable permissions and shebangs)
        "ERA", # eradicate (no commented-out code)
        "F",   # pyflakes (invalid Python code)
        "FBT", # flake8-boolean-trap (misusage of booleans in function declaration & calls)
        "G",   # flake8-logging-format (logging format strings)
        "I",   # isort (import order)
        "ICN", # flake8-import-conventions (how certain packages should be imported or aliased)
        # "INP", # flake8-no-pep420 (ban PEP-420 implicit namespace packages) -> long live implicit namespace packages!
        "INT", # flake8-gettext (f-string resolved before function calls)
        "ISC", # flake8-implicit-str-concat (string literal concatenation)
        "N",   # pep8-naming (naming conventions)
        "NPY", # NumPy-specific rules (e.g. deprecated-type-alias and legacy-random)
        "PD",  # pandas-vet (pandas code)
        "PIE", # flake8-pie (miscellaneous lints)
        "PGH", # pygrep-hooks (miscellaneous lints, e.g. "use specific rule codes when using noqa")
        "PL",  # Pylint (static code analyser)
        "PT",  # flake8-pytest-style (style issues or inconsistencies with pytest-based tests)
        "PTH", # flake8-use-pathlib (use of functions that can be replaced by pathlib module)
        "PYI", # flake8-pyi (provide specializations for type hinting stub files)
        "Q0",  # flake8-quotes (avoid escaping quotes)
        "RSE", # flake8-raise (improvements for raise statements)
        "RET", # flake8-return (check return values)
        "RUF", # ruff-specific rules
        "S",   # flake8-bandit (security)
        "SIM", # flake8-simplify (tips to simplify the code)
        "SLF", # flake8-self (private member access)
        "T10", # flake8-debugger
        "T20", # flake8-print (no print nor pprint)
        "TCH", # flake8-type-checking (move import only intended for type-checking in "if TYPE_CHECKING" blocs)
        "TID", # flake8-tidy-imports (ordonated imports)
        "TRY", # tryceratops (exception handling AntiPatterns)
        "UP",  # pyupgrade (upgrate syntax for newer versions of Python)
        "YTT", # flake8-2020 (misuse of sys.version and sys.version_info)
        "W",   # pycodestyle (violation of PEP-8)
    ]
    lint.ignore = [
        "ANN101",  # missing type annotation for self, but hinting self all the time is useless
        "ANN102",  # missing type annotation for cls but hinting cls all the time is useless
        "ANN401",  # disallows Any, but some elements should be Any when they are external
        "B024",    # forces abstract classes to have at least one abstract method, but sometimes a class is virtually abstract
        "D100",    # missing docstring in public module
        "D101",    # missing docstring in public class
        "D102",    # missing docstring in public method
        "D103",    # missing docstring in public function
        "D104",    # missing docstring in public package
        "D105",    # docstrings on magic methods, useless docstrings are well known
        "D107",    # missing docstring in __init__
        "DTZ007",  # allow use of datetime.datetime without timezone
        "DTZ011",  # naive datetime is used, but it's OK for the user to use it
        "ERA001",  # commented-out code is OK in some cases
        "E501",    # line size, but bug-bear already set it with a tolerance of 10% (B950)
        "PD901",   # allow use of `df` for dataframes
        "PD003",   # allow .isna() and .isnull() for dataframes
        "PD004",   # allow .notna() and .notnull() for dataframes
        "PD010",   # allow use of .pivot_table() for dataframes
        "PD015",   # allow use of .merge() for dataframes
        "PGH003",  # ignore use of specific rule codes when using noqa
        "PLR2004", # allow use of some magic constants
        "T201",    # allow print statements where necessary
        "TCH001",  # ignore import only for type-checking in "if TYPE_CHECKING" blocks
        "TCH002",  # ignore type-checking suggestions, trust the devs
        "UP007",   # ignore or-wise typing for py3.9 support
        "UP035",   # allow use of typing.Callable
    ]
    exclude = ["gunicorn_conf.py", "tests/", "scripts/"]

    line-length = 88
    indent-width = 4

    # Allow fix for all enabled rules (when `--fix`) is provided.
    fixable = ["ALL"]
    unfixable = []

    [tool.ruff.format]
    # Like Black, use double quotes for strings.
    quote-style = "double"

    # Like Black, indent with spaces, rather than tabs.
    indent-style = "space"

    # Like Black, respect magic trailing commas.
    skip-magic-trailing-comma = false

    # Like Black, automatically detect the appropriate line ending.
    line-ending = "auto"


    [tool.ruff.lint.per-file-ignores]
    "docs/conf.py" = [
        "A001", # redefine some builtins (like "copyright") is OK in docs
    ]
    ```

5. Nox, Ruff and Linters
"noxfile.py" = [
    "D402", # repeating the name of the function is OK for nox since it's to display it to the user
]
6. Pre-commit
7. GitHub workflows
