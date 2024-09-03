
# Contributing

Thanks for your interest in contributing to cpdfkit! Please take a moment to review this document **before submitting a pull request**.

## Pull requests

**Please ask first before starting work on any significant new features.**

It's never a fun experience to have your pull request declined after investing a lot of time and effort into a new feature. To avoid this from happening, we request that contributors create [a feature request](https://github.com/codingcowde/cpdfkit/discussions/new?category=ideas) to first discuss any new ideas. Your ideas and suggestions are welcome!

Please ensure that the tests are passing when submitting a pull request. If you're adding new features to cpdfkit, please include tests.

## Setting Up Your Local Development Environment

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/codingcowde/cpdfkit.git
cd cpdfkit
```

### 2. Create a Virtual Environment

It is recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3.  Install the Package Locally

To install the package in editable mode, run:

```bash
pip install -e .
```

This allows you to make changes to the source code and immediately see the effects without needing to reinstall the package.

## Running Tests

We use `unittest` for running tests. All tests are located in the `tests/` directory.

### 1. Running All Tests

You can run all tests using the following command:

```bash
python -m unittest discover tests
```

### 2. Running a Specific Test

To run a specific test file, use:

```bash
python -m unittest tests.test_chrome_pdf_toolkit
```

Make sure all tests pass before submitting a pull request.

## Where do I go from here?

For any questions, support, or ideas, etc., [please create a GitHub discussion](https://github.com/codingcowde/cpdfkit/discussions/new). If you've noticed a bug, [please submit an issue][new issue].

### Fork and create a branch

If this is something you think you can fix, then fork this repository and create a branch with a descriptive name.

### Implement your fix or feature

At this point, you're ready to make your changes. Feel free to ask for help.

### Create a Pull Request

If your changes look good and tests are passing, you are ready to create a pull request.

## Merging a PR (maintainers only)

A PR can only be merged into master by a maintainer if CI is passing, it is approved by another maintainer, and it is up to date with the default branch. Any maintainer is allowed to merge a PR if all of these conditions are met.

---
Credit: [nayafia](https://github.com/nayafia) for creating this amazing [CONTRIBUTE.md template](https://github.com/nayafia/contributing-template/)