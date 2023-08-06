# Pytest Workshop

## Installation

### Python

Maybe this [setting up python](https://wersdoerfer.de/blogs/ephes_blog/django-beginner-series-python/)
article is helpful.

### Clone Repository

```shell
git clone git@github.com:ephes/pytest-course.git
cd pytest-course
```

### Create Virtualenv

```shell
python -m pip install virtualenv
python -m virtualenv --prompt . venv
source venv/bin/activate  # bash and zsh
# source venv/bin/activate.fish
```

### Install pytest

```shell
python -m pip install pytest
```

### pre-commit

Install the pre-commit hooks:

```bash
python -m pip install pre-commit
pre-commit install
```
