import os
import shutil

##############################################################################
# Utilities
##############################################################################


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


##############################################################################
# Cookiecutter clean-up
##############################################################################

# Directive flags
no_github_actions = "{{cookiecutter.include_github_actions}}" == "no"
github_actions_ci = "{{cookiecutter.include_github_actions}}" == "ci"
no_docker = "{{cookiecutter.include_docker_support}}" == "no"
no_codeql_analysis = "{{cookiecutter.include_codeql_analysis}}" == "no"
no_stale_issues_bot = "{{cookiecutter.include_stale_issues_bot}}" == "no"
no_license = "{{cookiecutter.open_source_license}}" == "None"

# Remove workflow files (if specified)
if no_github_actions:
    remove(".github/")

# Remove CD workflow (if specified)
if github_actions_ci:
    remove(".github/workflows/continuous-deployment.yml")

# Remove Docker files (if specified)
if no_docker:
    remove(".github/workflows/docker-image-build.yml")
    remove("Dockerfile")
    remove(".dockerignore")
    remove("docker-entrypoint.sh")

# Remove CodeQL analysis (if specified)
if no_codeql_analysis:
    remove(".github/workflows/codeql-analysis.yml")

# Remove stale issues bot (if specified)
if no_stale_issues_bot:
    remove(".github/close-stale-issues.yml")

# Remove license (if specified)
if no_license:
    remove("LICENSE")
    remove("docs/license.md")
