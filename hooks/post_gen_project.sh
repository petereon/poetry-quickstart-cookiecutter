#!/bin/sh

# Initialize as git directory
git --version && git init

# Initialize pre-commit hooks
poetry --version && poetry install && poetry run pre-commit --version && 
poetry run pre-commit install --install-hooks -t commit-msg -t pre-push -t pre-commit

ln -s ../scripts/post-commit .git/hooks/post-commit