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

if "{{cookiecutter.include_github_actions}}" == "no":
    remove(".github/")
else:
    for root, dirs, files in os.walk(".github/workflows/"):
        for name in files:
            if not name.endswith("%s.yml" % "{{cookiecutter.include_github_actions}}"):
                remove(os.path.join(root, name))

# Remove license (if specified)
if "{{cookiecutter.open_source_license}}" == "None":
    remove("LICENSE")
