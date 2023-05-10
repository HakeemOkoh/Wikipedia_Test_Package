from WIKIFramework.base.DriverClass import WebDriverClass
import time
from WIKIFramework.base.BasePage import BaseClass
from WIKIFramework.pages.Landing import LandingPageClass


wd = WebDriverClass()

driver = wd.getWebDriver("chrome")
driver.maximize_window()
bp = BaseClass(driver)
lp = LandingPageClass(driver)
bp.launchWebPage("https://www.wikipedia.org/", "Wikipedia")
lp.languages()
lp.searching()
lp.listLanguages()
lp.donate()
lp.otherProjects()
lp.appLinks()
lp.footers()
time.sleep(3)
driver.quit()
