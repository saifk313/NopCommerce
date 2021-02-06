from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="./Drivers/chromedriver.exe")
        print("Launching Chrome")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="./Drivers/geckodriver")
        print("Launching Firefox")
    else:
        driver = webdriver.Chrome(executable_path="./Drivers/chromedriver.exe")
        print("Launching Chrome")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


############## Pytest HTML Report ##############

# A hook for adding Environment information to the HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = "Nop Commerce"
    config._metadata['Module Name'] = "Customers"
    config._metadata['Tester Name'] = "Saif"


# A hook for Modifying\Deleting Environment information to the HTML Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
