# poetry-quickstart-cookiecutter
Honed cookiecutter quickstart for my Python projects

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

From there, business as usual!

## Notes

- If you want to set up a SonarQube Scan, you will need to include a `SONAR_TOKEN` and `ACTIONS_TOKEN` in the repository secrets
- If you want to set up Deta deployment you will need an additional `DETA_TOKEN` and a file called `main.py` in `src/` folder importing or defining your `app` instance of FastAPI, Flask, or Starlette application
