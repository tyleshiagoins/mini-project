[![ci project](https://github.com/tyleshiagoins/mini-project/actions/workflows/ci.yml/badge.svg)](https://github.com/tyleshiagoins/mini-project/actions/workflows/ci.yml)

# Task Tracker

## Overview

Task tracker is a simple web application developed using python, flask, HTML, CSS, and javascript. It lets users to create a list of tasks through with a simple interface.


## Features

- **Add Tasks:** Enter a task and click the add task to add it to the list.
- **View Tasks:** All added tasks appear in the task list section.
- **Delete Tasks:** Remove tasks from the list using the delete option.
- **Empty List Message:** Displays a message when no tasks are present.

Tasks are stored temporarily in the browser and will be cleared when the page is refreshed or closed.

## Technologies Used

- Python and Flask 
- Git and GitHub 
- HTML and CSS — structure and styling
- JavaScript — functionality
- GitHub Actions — automated testing
- pytest and Flake8 — testing and code quality
- SonarCloud — security analysis

## How to Run the Application

**1. Install the required packages**

Open a terminal in the project's main directory and run:

```bash
python -m pip install -r task-tracker/requirements.txt
```

**2. Start the application**

```bash
python task-tracker/app.py
```

**3. Open the website**

Open the given address by doing Ctrl + click, and the application will be ready to use.


## Testing and Code Quality

The project uses pytest to test the python application and Flake8 to check coding standards.

To run the automated tests run this command:

```bash
python -m pytest --cov=greeting --cov=task-tracker --cov-report=term-missing --cov-fail-under=80
```

GitHub actions automatically runs checks when code is pushed or a pull request is opened. These checks include code formatting and SonarCloud security analysis.

The project uses a minimum test coverage requirement of 80%.