## Test Automation Homework on Pytest


### Getting started

Environment setup

Install requirements for tests execution

```bash
pip install -r requirements.txt
```

To run tests please run checker.py file

```bash
pytest -q pytest_project/pytest_homework/checker.py
```

If you'd like to see allure report, please make sure you have allure installed on your local machine, and run from cmd
```bash
pip install allure-pytest
pytest --alluredir=%allure_result_folder% pytest_project/pytest_homework/checker.py
allure serve pytest_project/pytest_homework/reports
```


