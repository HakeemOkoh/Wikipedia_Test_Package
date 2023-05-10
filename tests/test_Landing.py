import unittest
import pytest
import time
from WIKIFramework.base.BasePage import BaseClass
from WIKIFramework.pages.Landing import LandingPageClass


@pytest.mark.usefixtures("beforeClass","beforeMethod")
class LandingPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lp = LandingPageClass(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_landingPage(self):
        time.sleep(5)
        self.lp.languages()
        self.lp.searching()
        self.lp.listLanguages()
        self.lp.donate()
        self.lp.otherProjects()
        self.lp.appLinks()
        self.lp.footers()
        time.sleep(5)
