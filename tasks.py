import pathlib as plb
import shutil

from invoke import task

current_dir = plb.Path(__file__).absolute().parent


@task
def instantiate_template(c, cache_poetry_lock=False, cache_nox_dir=False):
    template_dir = current_dir / ".template"
    if not template_dir.exists():
        template_dir.mkdir()
    lock_file_cached = False
    nox_dir_cached = False
    if (template_dir / "mypkg").exists():
        print("Removing previously instantiated template ...")
        if cache_poetry_lock:
            if (current_dir / ".template" / "mypkg" / "poetry.lock").exists():
                lock_file_cached = True
                c.run("mv .template/mypkg/poetry.lock .template")
        if cache_nox_dir:
            if (current_dir / ".template" / "mypkg" / ".nox").exists():
                nox_dir_cached = True
                c.run("mv .template/mypkg/.nox .template")
        shutil.rmtree(template_dir / "mypkg")
    c.run(f"cookiecutter . --no-input --output-dir {str(current_dir / '.template')}")
    if lock_file_cached:
        c.run("mv .template/poetry.lock .template/mypkg")
    if nox_dir_cached:
        c.run("mv .template/.nox .template/mypkg")


@task
def update_pip(c):
    """This will update pip in the virtual environment"""
    c.run("poetry run python -m pip install -U pip")


@task(
    help={
        "dev": "Install development dependency group",
        "docs": "Install docs dependency group",
    }
)
def install_dependencies(c, dev=False, docs=False):
    """Install project dependencies and optional dependencies"""
    update_pip(c)
    cmd = "poetry install"
    if dev:
        cmd += " --with dev"
    if docs:
        cmd += " --with docs"
    c.run(cmd)


@task
def clean_artifacts(c):
    """This will clean python artifacts"""
    c.run('find . -type f -name "*.py[co]" -delete')
    c.run('find . -type d -name "__pycache__" -delete')


@task
def fmt_code(c, regen_template=True):
    """Format python code using black"""
    if regen_template:
        instantiate_template(c)
    print("--- FORMATTING CODE (black)")
    c.run("poetry run black -v --diff .template/mypkg")
    print("--- END CODE FORMATTING\n")


@task
def fmt_pyproject(c, regen_template=True):
    """Apply consistent formatting to pyproject"""
    if regen_template:
        instantiate_template(c)
    print("--- FORMATTING PYPROJECT (pyproject-fmt)")
    c.run("poetry run pyproject-fmt .template/mypkg/pyproject.toml")
    print("--- END PYPROJECT FORMATTING\n")


@task
def lint(c, regen_template=True):
    """Lint using flake8"""
    if regen_template:
        instantiate_template(c)
    print("--- LINTING CODE (flake8)")
    c.run(
        "poetry run flake8 .template/mypkg -v --extend-exclude .template/mypkg/.notebooks"
    )
    print("--- END LINTING\n")


@task
def check_type_hints(c, regen_template=True):
    """Check type hinting using mypy"""
    if regen_template:
        instantiate_template(c)
    print("--- TYPE CHECKS (mypy)")
    c.run(
        "cd .template/mypkg && poetry run mypy . --exclude .template/mypkg/.notebooks --ignore-missing-imports"
    )
    print("--- END TYPE CHECKS\n")


@task
def security_lint(c, regen_template=True):
    """Security linting using bandit"""
    if regen_template:
        instantiate_template(c)
    print("--- SECURITY LINTING (bandit)")
    c.run("poetry run bandit .template/mypkg -v")
    print("--- END SECURITY LINTING\n")


@task
def sort_imports(c, regen_template=True):
    """Sort python imports with isort"""
    if regen_template:
        instantiate_template(c)
    print("--- SORT IMPORTS (isort)")
    c.run(
        "poetry run isort -v .template/mypkg --skip .template/mypkg/.notebooks --diff"
    )
    print("--- END SORT IMPORTS\n")


@task
def check_docstring_coverage(c, regen_template=True):
    """Check docstring coverage using interrogate"""
    if regen_template:
        instantiate_template(c)
    print("--- DOCSTRING COVERAGE (interrogate)")
    c.run("poetry run interrogate -vv .template/mypkg/src")
    print("--- END DOCSTRING COVERAGE\n")


@task
def check_dependency_issues(c, regen_template=True):
    """Check dependency issues using deptry"""
    if regen_template:
        instantiate_template(c)
    print("--- CHECK DEPENDENCY ISSUES (deptry)")
    c.run("cd .template/mypkg && poetry run deptry src")
    print("--- END DEPENDENCY ISSUES\n")


@task
def build_docs(c, regen_template=True):
    """Build documentation using mkdocs"""
    if regen_template:
        instantiate_template(c)
    print("--- BUILDING DOCS (mkdocs)")
    c.run("cd .template/mypkg && mkdocs build")
    print("--- END BUILDING DOCS\n")


@task
def lock_dependencies(c, regen_template=True):
    """Check if project dependencies are compatible"""
    if regen_template:
        instantiate_template(c)
    print("--- LOCKING DEPENDENCIES")
    c.run("cd .template/mypkg && poetry lock -v")
    print("--- END LOCKING DEPENDENCIES")


@task
def checklist(c):
    """Instantiate the cookiecutter project and run checks"""
    instantiate_template(c)
    fmt_pyproject(c, regen_template=False)
    lock_dependencies(c, regen_template=False)
    check_dependency_issues(c, regen_template=False)
    security_lint(c, regen_template=False)
    check_docstring_coverage(c, regen_template=False)
    fmt_code(c, regen_template=False)
    lint(c, regen_template=False)
    sort_imports(c, regen_template=False)
    check_type_hints(c, regen_template=False)
    build_docs(c, regen_template=False)


@task
def test(c):
    """Run pytest on the 'tests' directory"""
    print("Running tests ...")
    c.run(f'poetry run coverage run -m pytest {str(current_dir / "tests")}')
    print("\n --- COVERAGE")
    c.run("poetry run coverage report -m")


@task
def coverage_report(c):
    """Generate coverage report"""
    c.run("poetry run coverage html")


@task
def nox(c, session="all", cache_nox_dir=True, cache_poetry_lock=False):
    """Run Noxfile in instantiated template"""
    instantiate_template(
        c, cache_nox_dir=cache_nox_dir, cache_poetry_lock=cache_poetry_lock
    )
    if not cache_poetry_lock:
        lock_dependencies(c, regen_template=False)
    cmd = "cd .template/mypkg && nox"
    if session != "all":
        cmd += f" -s {session}"
    c.run(cmd)


@task
def pre_commit(c, cache_poetry_lock=False):
    """Run pre-commit in instantiated template"""
    instantiate_template(c, cache_nox_dir=False, cache_poetry_lock=cache_poetry_lock)
    if not cache_poetry_lock:
        lock_dependencies(c, regen_template=False)
    c.run("cd .template/mypkg && poetry install --only dev")
    c.run("cd .template/mypkg && poetry run pre-commit install")
    c.run("cd .template/mypkg && poetry run pre-commit run --all")
