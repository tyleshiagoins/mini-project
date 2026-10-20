[![ci project](https://github.com/tyleshiagoins/mini-project/actions/workflows/ci.yml/badge.svg)](https://github.com/tyleshiagoins/mini-project/actions/workflows/ci.yml)

# Task Tracker - Midterm 

## Overview
This project is a simple web application used to track tasks and was created using Python and Flask. The project also includes work from previous mini-projects.

## Tools Used
- Python and Flask
- Git and GitHub
- GitHub Actions
- pytest
- Flake8
- SonarCloud

## How to Run the Application

These are the required packages

```bash
pip install -r task-tracker/requirements.txt
```

Start the application in the terminal with this line

```bash
python task-tracker/app.py
```

Copy and open the link to view the application

## Branching and Pull Requests
The main branch is used for the main version of the project, and new or test changes are made on the feature/midterm branch before being added to main.

## GitHub Actions
GitHub Actions is used to automatically check the project whenever code is pushed or a pull request is started.

The checks will install the packages, check code formatting, makes sure test coverage is at least 80%, checks that the Python files compile correctly, and uses SonarCloud to check code quality.

## Testing
The project includes tests for the original greeting program and the Task Tracker homepage.

Tests can be ran using the following command

```bash
python -m pytest --cov=greeting --cov=task-tracker --cov-report=term-missing --cov-fail-under=80
```

The latest local test run passed both tests with 93.33% total coverage.