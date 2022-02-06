# Changelog

<!--next-version-placeholder-->

## v0.3.0 (07/02/2022)

### ✨ NEW

- Refactor workflow files (#42)
  - Comments removed from steps and replaced with name keys
  - Workflow triggered on push/pull to any branch
  - CD job in the ci-cd.yaml workflow only triggers on push to main
  - PSR re-configured to patch release by default and to always make a GH release

### 📚 DOCS

- Add info about gh-pages hosting support (#40)

### 🐛 FIX

- Remove hard-coded pycounts name in CI/CD files (#38)

## v0.2.1 (06/12/2021)

### 🐛 FIX

- Removed hard-coded "pycounts" package name from CI/CD files.
- Renamed "cd" option to "ci+cd"

## v0.2.0 (06/09/2021)

### Breaking changes

- The new cookiecutter template has significantly changed since the last release. It has been modified to be in sync with and support the [Python Packages book](https://py-pkgs.org).

## v0.1.0 (16/08/2021)

- First release of `py-pkgs-cookiecutter`!