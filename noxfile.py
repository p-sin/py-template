import nox

# options
nox.options.sessions = (
    "pytest",
    "mypy",
    "ruff",
    "black",
    "coverage",
)
nox.options.reuse_existing_virtualenvs = True
SILENT_DEFAULT = True
SILENT_CODE_MODIFIERS = False
RUNNER = "poetry"

# targets
PACKAGE_LOCATION = "."
LEGACY_PYTHON_VERSIONS = ["3.6", "3.7", "3.8", "3.9"]
PYTHON_VERSIONS = ["3.10", "3.11", "3.12"]
PYPY3_VERSION = "pypy3"
LATEST_PYTHON = PYTHON_VERSIONS[-1]

@nox.session(python=PYTHON_VERSIONS, tags=["test"])
def pytest(session: nox.Session) -> None:
    """Run the test suite with pytest."""
    args = session.posargs or ("--cov", "-m", "not e2e")
    _install(session)
    _run(session, "pytest", *args)


@nox.session(python=LATEST_PYTHON, tags=["lint"])
def ruff(session: nox.Session) -> None:
    """Lint with ruff."""
    args = session.posargs or PACKAGE_LOCATION
    _install(session)
    _run(session, "ruff", "check", *args)


@nox.session(python=LATEST_PYTHON, tags=["format"])
def black(session: nox.Session) -> None:
    """Reformat with black."""
    args = session.posargs or PACKAGE_LOCATION
    _install(session)
    _run_code_modifier(session, "black", *args)


@nox.session(python=LATEST_PYTHON, tags=["format"])
def isort(session: nox.Session) -> None:
    """Reformat the import order with isort."""
    args = session.posargs or PACKAGE_LOCATION
    _install(session)
    _run_code_modifier(session, "isort", *args)


@nox.session(python=PYTHON_VERSIONS, tags=["typecheck"])
def mypy(session: nox.Session) -> None:
    """Verify types using mypy (so it is static)."""
    args = session.posargs or PACKAGE_LOCATION
    _install(session)
    _run(session, "mypy", *args)


@nox.session(python=LATEST_PYTHON, tags=["documentation"])
def docs(session: nox.Session) -> None:
    """Build the documentation."""
    _install(session)
    _run(session, "sphinx-build", "docs", "docs/_build")


@nox.session(python=LATEST_PYTHON, tags=["ci"])
def coverage(session: nox.Session) -> None:
    """Upload coverage data."""
    args = session.posargs or [
        "--cov",
        "-m",
        "not e2e",
        "--cov-report=xml",
        "--cov-fail-under=0",
    ]
    _install(session)
    _run(session, "pytest", *args)


def _install(session: nox.Session, *args: str) -> None:
    session.run(RUNNER, "install", *args, external=True, silent=SILENT_DEFAULT)


def _run(
    session: nox.Session,
    target: str,
    *args: str,
    silent: bool = SILENT_DEFAULT,
) -> None:
    session.run(RUNNER, "run", target, *args, external=True, silent=silent)


def _run_code_modifier(session: nox.Session, target: str, *args: str) -> None:
    _run(session, target, *args, silent=SILENT_CODE_MODIFIERS)
