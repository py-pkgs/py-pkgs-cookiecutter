import os
import shutil
import requests
from textwrap import dedent

##############################################################################
# Utilities
##############################################################################

border = "=" * 79
endc = "\033[0m"
bcolors = dict(
    blue="\033[94m",
    green="\033[92m",
    orange="\033[93m",
    red="\033[91m",
    bold="\033[1m",
    underline="\033[4m",
)


def _color_message(msg, style):
    return bcolors[style] + msg + endc


def _message_box(msg, color="green", doprint=True, print_func=print):
    # Prepare the message so the indentation is the same as the box
    msg = dedent(msg)

    # Color and create the box
    border_colored = _color_message(border, color)
    box = """
    {border_colored}
    {msg}
    {border_colored}
    """
    box = dedent(box).format(msg=msg, border_colored=border_colored)
    if doprint is True:
        print_func(box)
    return box


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


##############################################################################
# Cookiecutter clean-up
##############################################################################

# Directive flags
no_workflow = "{{cookiecutter.include_github_actions}}" == "no"
build_workflow = "{{cookiecutter.include_github_actions}}" == "build"
license = "{{cookiecutter.open_source_license}}" == "None"

# Remove workflow files (if specified)
if no_workflow:
    # remove top-level file inside the generated folder
    remove(".github/")
elif build_workflow:
    remove(".github/workflows/deploy.yml")

# Remove license (if specified)
if license:
    remove("LICENSE")

# Check GitHub username
if (
    not requests.get(
        "http://www.github.com/{{cookiecutter.github_username}}"
    ).status_code
    < 400
):
    _message_box(
        "WARNING:\n"
        "Template successfully created but the user '{{cookiecutter.github_username}}' does\n"
        "not exist on github.com. Please check the 'github_username' entered.\n"
        "If you won't be using github.com you may ignore this warning.",
        color="orange",
    )