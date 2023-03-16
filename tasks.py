import pathlib as plb
import shutil

from invoke import task

current_dir = plb.Path(__file__).absolute().parent


@task
def instantiate_template(c):
    template_dir = current_dir / ".template"
    if not template_dir.exists():
        template_dir.mkdir()
    if (template_dir / "mypkg").exists():
        shutil.rmtree(template_dir / "mypkg")
    c.run(f"cookiecutter . --no-input --output-dir {str(current_dir / '.template')}")


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
def clean(c):
    """This will clean python artifacts"""
    c.run('find . -type f -name "*.py[co]" -delete')
    c.run('find . -type d -name "__pycache__" -delete')


@task
def fmt(c, regen_template=True):
    """Format python code using black"""
    if regen_template:
        instantiate_template(c)
    print('--- FORMATTING CODE (black)')
    c.run("poetry run black -v --diff .template/mypkg")
    print('--- END CODE FORMATTING\n')


@task
def pyproject_fmt(c, regen_template=True):
    """Apply consistent formatting to pyproject"""
    if regen_template:
        instantiate_template(c)
    print('--- FORMATTING PYPROJECT (pyproject-fmt)')
    c.run("poetry run pyproject-fmt .template/mypkg/pyproject.toml")
    print('--- END PYPROJECT FORMATTING\n')    
    

@task
def lint(c, regen_template=True):
    """Lint using flake8"""
    if regen_template:
        instantiate_template(c)
    print('--- LINTING CODE (flake8)')
    c.run("poetry run flake8 .template/mypkg -v --extend-exclude .template/mypkg/.notebooks")
    print('--- END LINTING\n')


@task
def type_hints(c, regen_template=True):
    """Check type hinting using mypy"""
    if regen_template:
        instantiate_template(c)
    print('--- TYPE CHECKS (mypy)')
    c.run("poetry run mypy .template/mypkg --exclude .template/mypkg/.notebooks --ignore-missing-imports")
    print('--- END TYPE CHECKS\n')


@task
def security_lint(c, regen_template=True):
    """Security linting using bandit"""
    if regen_template:
        instantiate_template(c)
    print('--- SECURITY LINTING (bandit)')
    c.run('bandit .template/mypkg -v')
    print('--- END SECURITY LINTING\n')


@task
def sort_imports(c, regen_template=True):
    """Sort python imports with isort"""
    if regen_template:
        instantiate_template(c)
    print('--- SORT IMPORTS (isort)')
    c.run("poetry run isort -v .template/mypkg --skip .template/mypkg/.notebooks")
    print('--- END SORT IMPORTS\n')


@task
def docstring_coverage(c, regen_template=True):
    """Check docstring coverage using interrogate"""
    if regen_template:
        instantiate_template(c)
    print('--- DOCSTRING COVERAGE (interrogate)')
    c.run("poetry run interrogate -vv .template/mypkg/src")
    print('--- END DOCSTRING COVERAGE\n')


@task
def check_dependencies(c, regen_template=True):
    """Check dependency issues using deptry"""
    if regen_template:
        instantiate_template(c)
    print('--- CHECK DEPENDENCY ISSUES (deptry)')
    c.run("cd .template/mypkg && poetry run deptry src")
    print('--- END DEPENDENCY ISSUES\n')    


@task
def build_docs(c, regen_template=True):
    """Build documentation using mkdocs"""
    if regen_template:
        instantiate_template(c)
    print('--- BUILDING DOCS (mkdocs)')
    c.run("cd .template/mypkg && mkdocs build")
    print('--- END BUILDING DOCS\n')


@task
def lock_dependencies(c, regen_template=True):
    """Check if project dependencies are compatible"""
    if regen_template:
        instantiate_template(c)
    print('--- LOCKING DEPENDENCIES')
    c.run("cd .template/mypkg && poetry lock -v")
    print('--- END LOCKING DEPENDENCIES')


@task
def checklist(c):
    """Instantiate the cookiecutter project and run checks"""
    instantiate_template(c)
    pyproject_fmt(c, regen_template=False)
    lock_dependencies(c, regen_template=False)
    check_dependencies(c, regen_template=False)
    security_lint(c, regen_template=False)
    docstring_coverage(c, regen_template=False)
    fmt(c, regen_template=False)
    lint(c, regen_template=False)
    sort_imports(c, regen_template=False)
    type_hints(c, regen_template=False)
    build_docs(c, regen_template=False)
    

@task
def test(c):
    """Run pytest on the 'tests' directory"""
    print("Running tests ...")
    c.run(f'poetry run coverage run -m pytest {str(current_dir / "tests")}')
    print("\n --- COVERAGE")
    c.run('poetry run coverage report -m')


@task
def coverage_report(c):
    """Generate coverage report"""
    c.run('poetry run coverage html')
