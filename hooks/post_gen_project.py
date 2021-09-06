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
no_license = "{{cookiecutter.open_source_license}}" == "None"

# Remove workflow files (if specified)
if no_github_actions:
    remove(".github/")
elif github_actions_ci:
    remove(".github/workflows/ci-cd.yml")
else:
    remove(".github/workflows/ci.yml")

# Remove license (if specified)
if no_license:
    remove("LICENSE")
