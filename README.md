# poetry-quickstart-cookiecutter
Honed cookiecutter quickstart for Python projects

## Overview

This cookie-cutter aims to bring `npm` levels of automation and simplicity to the life of Python developer, it is focused on productivity without compromises. It tries to be the `Mac` of cookie-cutters

- It is infused with several years of professional experience with Python.
- It strives to be powerful without feeling heavy.
- It's tries to abstract away all the different tools and names into simple commands like `lint` or `test`.
- It comes `watch` commands, allowing continuous testing and linting.
- It comes pre-fitted with powerful set of linting and testing tools ready to help you build rock-solid state-of-art Python application.
- It comes with opinionated config, so that you can focus on what's important - programming.

## Setup

Poetry and Cookiecutter are required as depencies, it is recommended to install them with `pipx`
```sh
pipx install poetry cookiecutter
```

This repo can be used as a template using:
```sh
cookiecutter https://github.com/petereon/poetry-quickstart-cookiecutter.git
```

### Notes

- If you want to set up a SonarQube Scan, you will need to include a `SONAR_TOKEN` and `ACTIONS_TOKEN` in the repository secrets
- If you want to set up Deta deployment you will need an additional `DETA_TOKEN` and a file called `main.py` in `src/` folder importing or defining your `app` instance of FastAPI, Flask, or Starlette application

## Usage

There are `poe` tasks defined for most of the common needs:

- `poe test` which runs the ward unit tests
- `poe test:watch` which runs `poe test` in watch mode
- `poe lint` which runs several linting solutions
- `poe lint:watch` which runs `poe lint` in watch mode
- `poe lint:perf` which runs `poe lint` and `perflint`
- `poe bdd` which runs the behave bdd tests
- `poe bdd:watch` which runs `poe bdd` in watch mode
- `poe test:all` which runs `poe test` and `poe bdd`