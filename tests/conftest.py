import pytest
from WIKIFramework.base.BasePage import BaseClass
from WIKIFramework.base.DriverClass import WebDriverClass
import time


@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    wdc = WebDriverClass()
    driver = wdc.getWebDriver("chrome")
    bp = BaseClass(driver)
    bp.launchWebPage("https://www.wikipedia.org/", "Wikipedia")
    driver.maximize_window()
    if request.cls is not None:  # cls = class level object, so driver is available to all classes in tests package
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')


@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')