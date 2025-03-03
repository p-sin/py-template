import nox

# options
nox.options.sessions = (
    "pytest",
    "mypy",
    "ruff",
    "black",
    "isort",
    "coverage",
    "bandit",
    "safety",
    "pip_audit",
    "checkov",
    "hadolint",
    "docs",
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


@nox.session(python=LATEST_PYTHON, tags=["lint"])
def ruff(session: nox.Session) -> None:
    """Lint with ruff."""
    _install(session, "ruff")
    _run(session, "ruff", "check", PACKAGE_LOCATION)


@nox.session(python=LATEST_PYTHON, tags=["format"])
def black(session: nox.Session) -> None:
    """Reformat with black."""
    _install(session, "black")
    _run_code_modifier(session, "black", PACKAGE_LOCATION)


@nox.session(python=LATEST_PYTHON, tags=["format"])
def isort(session: nox.Session) -> None:
    """Sort imports with isort."""
    _install(session, "isort")
    _run_code_modifier(session, "isort", PACKAGE_LOCATION)


@nox.session(python=PYTHON_VERSIONS, tags=["test"])
def pytest(session: nox.Session) -> None:
    """Run the test suite with pytest."""
    args = session.posargs or ("--cov", "-m", "not e2e")
    _install(session, "pytest", "pytest-cov")
    _run(session, "pytest", *args)


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
    _install(session, "pytest", "pytest-cov")
    _run(session, "pytest", *args)


def hadolint(session: nox.Session) -> None:
    """Lint Dockerfile with Hadolint."""
    _install(session)
    _run(session, "hadolint", "Dockerfile")


@nox.session(python=PYTHON_VERSIONS, tags=["typecheck"])
def mypy(session: nox.Session) -> None:
    """Verify types using mypy (so it is static)."""
    _install(session, "mypy")
    _run(session, "mypy", PACKAGE_LOCATION)


@nox.session(python=LATEST_PYTHON, tags=["security"])
def bandit(session: nox.Session) -> None:
    """Run Bandit security checks."""
    _install(session, "bandit")
    _run(session, "bandit", "-r", PACKAGE_LOCATION)


@nox.session(python=LATEST_PYTHON, tags=["security"])
def safety(session: nox.Session) -> None:
    """Check dependencies for vulnerabilities."""
    _install(session, "safety")
    _run(session, "safety", "check")


@nox.session(python=LATEST_PYTHON, tags=["security"])
def pip_audit(session: nox.Session) -> None:
    """Run pip-audit to check for vulnerable dependencies."""
    _install(session, "pip-audit")
    _run(session, "pip-audit")


@nox.session(python=LATEST_PYTHON, tags=["security"])
def checkov(session: nox.Session) -> None:
    """Run Checkov to scan infrastructure as code (IaC)."""
    _install(session, "checkov")
    _run(session, "checkov", "--directory", PACKAGE_LOCATION)


@nox.session(python=LATEST_PYTHON, tags=["security"])
def trufflehog(session: nox.Session) -> None:
    """Scan repository for secrets."""
    _install(session, "trufflehog")
    _run(session, "trufflehog", "--regex", "--entropy=True", PACKAGE_LOCATION)


@nox.session(python=LATEST_PYTHON, tags=["documentation"])
def docs(session: nox.Session) -> None:
    """Build Sphinx documentation."""
    _install(session, "sphinx")
    _run(session, "sphinx-build", "docs", "docs/_build")


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
