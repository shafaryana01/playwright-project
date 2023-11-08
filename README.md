# WebApp UI test automation

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
  - [Setup](#setup)
- [Usage](#usage)
  - [Running tests](#running)
  - [Debugging tests](#debugging)
  - [Reports](#reports)


## About <a id="about"></a>
This repository contains the code of end-to-end tests, written in Playwright framework (https://playwright.dev/python/).
Main pattern used for this project - is Page Object. We describe elements of pages, actions, which we use to interact 
with pages (*pages* folder). And describe test specs (*tests* folder) - things/flows we want to test and verify on 
our pages.

There are several main folders of these project:
* pages - contains classes, which describe what elements different pages have and how pages can behave
* tests - contains test specs

## Getting started <a id="getting_started"></a>

### Setup <a id="setup"></a>
1. Clone repo
2. Create virtual environment
Run `python -m venv myenv`
then `myenv\Scripts\activate`
3. Install packages. Run `pip install -r requirements.txt`
4. Install playwright. Run `playwright install`
5. Add `.env` file to the root of project and add data to this file based on `.env.example`

## Usage <a id="usage"></a>

### Running tests <a id="running"></a>

* General way to run all playwright tests to run `pytest` command. This command will run all existing test spec headless
in browsers. 
```
pytest
```
* To run a single test file run `pytest test_shopping_cart.py` and pass in the name of the test file that 
you want to run.
```
pytest test_shopping_cart.py
```
* To run tests in headed mode go to `pytest.ini` file and in `addopts` indicate `--headed`.
* To run tests in a specific browser go to `pytest.ini` file and in `addopts` with the help of `--browser` 
indicate browsers.

### Debugging tests <a id="debugging"></a>
#### For Linux
* To debug all tests run `PWDEBUG=1 pytest -s` command. This command will open up a Browser window as well as 
the Playwright Inspector. You can use the step over button at the top of the inspector to step through your test. 
Or press the play button to run your test from start to finish. Once the test has finished the browser window will close.
```
PWDEBUG=1 pytest -s
```
* To debug one test run `PWDEBUG=1 pytest -s test_shopping_cart.py` followed by the name of the test file that you want 
to debug.
```
PWDEBUG=1 pytest -s test_shopping_cart.py
```

#### For Windows
* To debug tests on windows set env variable PWDEBUG using `$env:PWDEBUG="1"` command. Then run Pytest command to run tests.
```
$env:PWDEBUG="1"
```
```
pytest
```
* To set debug mode off, use `$env:PWDEBUG="0"`
```
$env:PWDEBUG="0"
```

### Reports <a id="reports"></a>
* To get HTML Report in `pytest.ini` file indicated `--html=pwreport1.html` option. After running tests *pwreport.html* 
file will appear.
* To get Allure Report in `pytest.ini` file indicated `--alluredir allure-results` option. After running tests 
*allure-results* folder will appear. After that run `allure serve allure-results` command.
```
allure serve allure-results
```
