# poetry-quickstart-cookiecutter
Honed cookiecutter quickstart for my Python projects

## Setup

Poetry and Cookiecutter are required as depencies, it is recommended to install them with `pipx`
```sh
pipx install poetry cookiecutter
```

This repo can be used as a template using:
```sh
cookiecutter https://github.com/petereon/poetry-quickstart-cookiecutter.git
```

Then dependencies can be installed using
```sh
poetry install
```

To setup precommit:
```sh
precommit install && pre-commit install --hook-type commit-msg
```

### Notes

- If you want to set up a SonarQube Scan, you will need to include a `SONAR_TOKEN` and `ACTIONS_TOKEN` in the repository secrets
- If you want to set up Deta deployment you will need an additional `DETA_TOKEN` and a file called `main.py` in `src/` folder importing or defining your `app` instance of FastAPI, Flask, or Starlette application

## Usage

There are `poe` tasks defined for most of the common needs:
- `poe add` to add packages, which just duplicates `poetry add` for convenience
- `poe install` to install the poetry deps from `pyproject.toml`
- `poe build` to build a `.whl` package from the project
- `poe clean` which deletes build artifacts and caches
- `poe test` which runs the pytest
- `poe test-lint` running pytest with additional `--mypy --black` flags to report linting and fromatting issues
- `poe format` which runs `black` to format the code
- `poe lint` which runs `mypy` to lint the code and report linting issues
