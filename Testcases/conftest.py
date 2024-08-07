import pytest
from selenium import webdriver


def pytest_addoption(parser):  # add custom command liner for browser
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("lunching the Chrome webbrowesr")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("lunching the Firefox webbrowser")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("lunching the edge webbrowser")
    else:
        print("lunching the headless browser")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver

def pytest_metadata(metadata):
    metadata["project_name"]="OrangeHRM_login_DDT"
    metadata["Testcase"]="DDT user login Automation"
    metadata["Tester_name"]="Ravikant.Suryawanshi"
    metadata.pop("plugines",None)