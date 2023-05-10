from selenium import webdriver
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service
import WIKIFramework.utilities.CustomLogger as cl


class WebDriverClass:

    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            driver = webdriver.Chrome("../configurationfiles/BrowserDrivers/chromedriver.exe")
            self.log.info("Chrome Driver is initializing")
        elif browserName == "edge":
            driver = webdriver.Edge("../configurationfiles/BrowserDrivers/msedgedriver.exe")
            self.log.info("Edge Driver is initializing")
        elif browserName == "firefox":
            options = FirefoxOptions()
            options.headless = False
            service = Service("../configurationfiles/BrowserDrivers/geckodriver.exe")
            driver = Firefox(service=service, options=options)
            self.log.info("FireFox Driver is initializing")

        return driver
