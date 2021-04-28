.. highlight:: shell

==========
Quickstart
==========

1. Install the latest Cookiecutter if you haven't installed it yet:

    .. prompt:: bash

        poetry install

2. Generate a Python package file and directory structure:

    .. prompt:: bash

        cookiecutter https://github.com/UBC-MDS/cookiecutter-ubc-mds.git
   
3. Install the required development dependencies:

    .. prompt:: bash

        poetry add --dev pytest pytest-cov codecov python-semantic-release flake8 sphinx sphinxcontrib-napoleon nbsphinx ipykernel
  
4. Create a remote version control repository on GitHub for this project, and link it to `<https://codecov.io/>`_. Get the repository token from `<https://codecov.io/>`_ and record is as a secret on GitHub using the name `CODECOV_TOKEN`.
    
5. Write the code and tests for your Python package! And use Python poetry to install, add dependencies and test your package locally. For more details, see the `Python Packages book <https://py-pkgs.org>`_.

6. Render your documentation:

    .. prompt:: bash

        poetry run sphinx-apidoc -f -o docs/source <your_project>
        cd docs
        poetry run make html

7. Put your local files under version control with Git, add the GitHub repository you set up as the remote and push your changes to GitHub! 

8. To have your docs appear on Read the Docs, follow the `instructions in the Python Packages book <https://py-pkgs.org/03-how-to-package-a-python#reading-and-rendering-documentation-remotely>`_.

9. When you are satisfied, use poetry to publish your package to testPyPI.


(Optional) Automated version bumping and releasing to test PyPI
---------------------------------------------------------------

10. Add the following to the `pyproject.toml` file (substituting <your_project> with the appropriate value):

    .. code-block:: toml

        [tool.semantic_release]
        version_variable = "<your_project>/__init__.py:__version__"
        version_source = "commit"
        upload_to_pypi = "false"
        patch_without_tag = "true"

11. Add the following secrets to the project's repository on GitHub:

    - TEST_PYPI_USERNAME
    - TEST_PYPI_PASSWORD

12. Put your local files under version control with Git, add the GitHub repository you set up as the remote and push your changes to GitHub and Let the magic happen! For more details, see the `Python Packages book <https://py-pkgs.org>`_.

(Optional) Push to PyPI
-----------------------

13. Once you are happy with the state of your package, and you want to publish to PyPI as opposed to testPyPI, all you need to do is add your PYPI_USERNAME & PYPI_PASSWORD to your project repo as GitHub secrets and change `this line <https://github.com/UBC-MDS/cookiecutter-ubc-mds/blob/bd8cb34f83d6341c411954322354031602606b80/%7B%7Bcookiecutter.project_slug%7D%7D/.github/workflows/deploy.yml#L74>`_ of the release GitHub Actions workflow to this:

    .. prompt:: bash

        poetry publish -u $PYPI_USERNAME -p $PYPI_PASSWORD


(Optional) Continuous deployment when master branch protection is enabled
-------------------------------------------------------------------------

14. If you want to use the `deploy.yml` GitHub Actions workflow (which performs automated version bumping, package building and publishing to (test) PyPI) provided by this Cookicutter template with a repository where you have enabled master branch protection (and also applied this rule to administrators), you will need to add two addtional steps to `deploy.yml`. The reason for this, is that this workflow (which bumps versions and deploy the package) is triggered to run **after** the pull request is merged to master. Therefore, when we bump the versions in the `pyproject.toml` file and the `package/__init__.py` file (the two places in our package where the version must be stored) we need to push these changes to the master branch - however this is problematic given that we have set-up master branch protection!

    What are we to do? The most straightforward thing appears to be to use a bot to briefly turn off master branch protection just before we push the files where we bumped the version, and then use the bot to turn it back on again after pushing. To do this, we will use the `benjefferies/branch-protection-bot action <https://github.com/benjefferies/branch-protection-bot>`_.

    Looking at `deploy.yml <https://github.com/UBC-MDS/cookiecutter-ubc-mds/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/.github/workflows/deploy.yml>`_, we will add the `branch-protection-bot` action to **turn off** master branch protection after the step named "checkout" but before the step named "Bump package versions". We will also add the `branch-protection-bot` action to **turn on** master branch protection after the step named "Push package version changes" but before the step named "Get release tag version from package version".

    Below is the section of our `deploy.yml <https://github.com/UBC-MDS/cookiecutter-ubc-mds/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/.github/workflows/deploy.yml>`_ **before** we add the `branch-protection-bot`:
    
    .. code-block:: yaml

        - name: checkout
          uses: actions/checkout@master
          with:
              ref: master
              fetch-depth: '0'
        - name: Bump package versions
          run: |
              git config --local user.email "action@github.com"
              git config --local user.name "GitHub Action"
              poetry run semantic-release version
              poetry version $(grep "version" */__init__.py | cut -d "'" -f 2 | cut -d '"' -f 2)
              git commit -m "Bump versions" -a
        - name: Push package version changes
          uses: ad-m/github-push-action@master
          with:
              github_token: ${{ secrets.GITHUB_TOKEN }}
        - name: Get release tag version from package version
          run: |
              echo ::set-output name=release_tag::$(grep "version" */__init__.py | cut -d "'" -f 2 | cut -d '"' -f 2)
          id: release
    
    Below is the section of our `deploy.yml <https://github.com/UBC-MDS/cookiecutter-ubc-mds/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/.github/workflows/deploy.yml>`_ **after** we add the `branch-protection-bot`:
    
    .. code-block:: yaml

        - name: checkout
          uses: actions/checkout@master
          with:
              ref: master
              fetch-depth: '0'
        - name: Temporarily disable "include administrators" branch protection
          uses: benjefferies/branch-protection-bot@master
          if: always()
          with:
              access-token: ${{ secrets.ACCESS_TOKEN }}
        - name: Bump package versions
          run: |
              git config --local user.email "action@github.com"
              git config --local user.name "GitHub Action"
              poetry run semantic-release version
              poetry version $(grep "version" */__init__.py | cut -d "'" -f 2 | cut -d '"' -f 2)
              git commit -m "Bump versions" -a
        - name: Push package version changes
          uses: ad-m/github-push-action@master
          with:
              github_token: ${{ secrets.GITHUB_TOKEN }}
        - name: Enable "include administrators" branch protection
          uses: benjefferies/branch-protection-bot@master
          if: always()  # Force to always run this step to ensure "include administrators" is always turned back on
          with:
              access-token: ${{ secrets.ACCESS_TOKEN }}
              owner: <github_username_or_org>
              repo: <github_repo_name>
        - name: Get release tag version from package version
          run: |
              echo ::set-output name=release_tag::$(grep "version" */__init__.py | cut -d "'" -f 2 | cut -d '"' -f 2)
          id: release
    
    Finally, to make this work you will need to add one of your team members personal GitHub access tokens as a GitHub secret named `ACCESS_TOKEN` (see `here <https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line>`_ for how to get your personal GitHub access token).