import json

from WIKIFramework.base.BasePage import BaseClass
import WIKIFramework.utilities.CustomLogger as cl


class LandingPageClass(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    with open("C:/Users/HAKEEM/PycharmProjects/WIKIPEDIA/WIKIFramework/pages/elements.json", "r") as infile:
        elements = json.load(infile)

    def languages(self):
        for i in range(10):
            english = self.isElementDisplayed(self.elements["_english"]["locatorValue"], "id")
            assert english == True
            self.clickOnElement(self.elements["_english"]["locatorValue"], "id")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on English Language Option")
            self.driver.back()

            japanese = self.isElementDisplayed(self.elements["_japanese"]["locatorValue"], "id")
            assert japanese == True
            self.clickOnElement(self.elements["_japanese"]["locatorValue"], "id")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Japanese Language Option")
            self.driver.back()

            spanish = self.isElementDisplayed(self.elements["_spanish"]["locatorValue"], "id")
            assert spanish == True
            self.clickOnElement(self.elements["_spanish"]["locatorValue"], "id")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Spanish Language Option")
            self.driver.back()

            italian = self.isElementDisplayed(self.elements["_italian"]["locatorValue"], "id")
            assert italian == True
            self.clickOnElement(self.elements["_italian"]["locatorValue"], "id")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Italian Language Option")
            self.driver.back()

            farsi = self.isElementDisplayed(self.elements["_farsi"]["locatorValue"], "id")
            assert farsi == True
            self.clickOnElement(self.elements["_farsi"]["locatorValue"], "id")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Farsi Language Option")
            self.driver.back()

            russian = self.isElementDisplayed(self.elements["_russian"]["locatorValue"], "id")
            assert russian == True
            self.clickOnElement(self.elements["_russian"]["locatorValue"], "id")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Russian Language Option")
            self.driver.back()

            german = self.isElementDisplayed(self.elements["_german"]["locatorValue"], "id")
            assert german == True
            self.clickOnElement(self.elements["_german"]["locatorValue"], "id")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on German Language Option")
            self.driver.back()

            french = self.isElementDisplayed(self.elements["_french"]["locatorValue"], "id")
            assert french == True
            self.clickOnElement(self.elements["_french"]["locatorValue"], "id")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on French Language Option")
            self.driver.back()

            chinese = self.isElementDisplayed(self.elements["_chinese"]["locatorValue"], "id")
            assert chinese == True
            self.clickOnElement(self.elements["_chinese"]["locatorValue"], "id")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Chinese Language Option")
            self.driver.back()

            portuguese = self.isElementDisplayed(self.elements["_portuguese"]["locatorValue"], "id")
            assert portuguese == True
            self.clickOnElement(self.elements["_portuguese"]["locatorValue"], "id")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Portuguese Language Option")
            self.driver.back()

            return

    def searching(self):
        for i in range(3):
            searchInputBar = self.isElementDisplayed(self.elements["_searchInputBar"]["locatorValue"], "id")
            assert searchInputBar == True
            self.sendText("Mutagenesis", self.elements["_searchInputBar"]["locatorValue"], "id")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Sent a query")
            self.driver.back()
            self.getWebElement(self.elements["_searchInputBar"]["locatorValue"], "id").clear()

            self.clickOnElement(self.elements["_languageDropDown"]["locatorValue"], "id")
            self.driver.implicitly_wait(5)
            cl.allureLogs("Clicked on Search Language Drop Down button")
            self.clickOnElement(self.elements["_languageDropDown"]["locatorValue"], "id")

            self.clickOnElement(self.elements["_searchButton"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Search button")
            self.driver.back()

            return

    def listLanguages(self):
        languageList = self.isElementDisplayed(self.elements["_listLanguages"]["locatorValue"], "id")
        assert languageList == True
        self.clickOnElement(self.elements["_listLanguages"]["locatorValue"], "id")
        self.driver.implicitly_wait(5)
        cl.allureLogs("Clicked on Read in your Language Button")
        self.clickOnElement(self.elements["_listLanguages"]["locatorValue"], "id")

    def donate(self):
        self.scrollTo(self.elements["_donate"]["locatorValue"], "css")
        donate = self.isElementDisplayed(self.elements["_donate"]["locatorValue"], "css")
        assert donate == True
        self.clickOnElement(self.elements["_donate"]["locatorValue"], "css")
        self.driver.implicitly_wait(10)
        self.windowhandling()
        cl.allureLogs("Successfully opened and closed 'You can support our work with a donation' page")

    def otherProjects(self):
        for i in range(12):
            self.scrollTo(self.elements["_commons"]["locatorValue"], "css")
            commons = self.isElementDisplayed(self.elements["_commons"]["locatorValue"], "css")
            assert commons == True
            self.clickOnElement(self.elements["_commons"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Commons Button")
            self.driver.back()

            self.scrollTo(self.elements["_wikivoyage"]["locatorValue"], "css")
            wikivoyage = self.isElementDisplayed(self.elements["_wikivoyage"]["locatorValue"], "css")
            assert wikivoyage == True
            self.clickOnElement(self.elements["_wikivoyage"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Wikivoyage Button")
            self.driver.back()

            self.scrollTo(self.elements["_wiktionary"]["locatorValue"], "css")
            wiktionary = self.isElementDisplayed(self.elements["_wiktionary"]["locatorValue"], "css")
            assert wiktionary == True
            self.clickOnElement(self.elements["_wiktionary"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Wiktionary Button")
            self.driver.back()

            self.scrollTo(self.elements["_wikibooks"]["locatorValue"], "css")
            wikibooks = self.isElementDisplayed(self.elements["_wikibooks"]["locatorValue"], "css")
            assert wikibooks == True
            self.clickOnElement(self.elements["_wikibooks"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Wikibooks Button")
            self.driver.back()

            self.scrollTo(self.elements["_wikinews"]["locatorValue"], "css")
            wikinews = self.isElementDisplayed(self.elements["_wikinews"]["locatorValue"], "css")
            assert wikinews == True
            self.clickOnElement(self.elements["_wikinews"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Wikinews Button")
            self.driver.back()

            self.scrollTo(self.elements["_wikidata"]["locatorValue"], "css")
            wikidata = self.isElementDisplayed(self.elements["_wikidata"]["locatorValue"], "css")
            assert wikidata == True
            self.clickOnElement(self.elements["_wikidata"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Wikidata Button")
            self.driver.back()

            self.scrollTo(self.elements["_wikiversity"]["locatorValue"], "css")
            wikiversity = self.isElementDisplayed(self.elements["_wikiversity"]["locatorValue"], "css")
            assert wikiversity == True
            self.clickOnElement(self.elements["_wikiversity"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Wikiversity Button")
            self.driver.back()

            self.scrollTo(self.elements["_wikiqoute"]["locatorValue"], "css")
            wikiqoute = self.isElementDisplayed(self.elements["_wikiqoute"]["locatorValue"], "css")
            assert wikiqoute == True
            self.clickOnElement(self.elements["_wikiqoute"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Wikiqoute Button")
            self.driver.back()

            self.scrollTo(self.elements["_mediaWiki"]["locatorValue"], "css")
            mediaWiki = self.isElementDisplayed(self.elements["_mediaWiki"]["locatorValue"], "css")
            assert mediaWiki == True
            self.clickOnElement(self.elements["_mediaWiki"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on MediaWiki Button")
            self.driver.back()

            self.scrollTo(self.elements["_wikisource"]["locatorValue"], "css")
            wikisource = self.isElementDisplayed(self.elements["_wikisource"]["locatorValue"], "css")
            assert wikisource == True
            self.clickOnElement(self.elements["_wikisource"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Wikisource Button")
            self.driver.back()

            self.scrollTo(self.elements["_wikispecies"]["locatorValue"], "css")
            wikispecies = self.isElementDisplayed(self.elements["_wikispecies"]["locatorValue"], "css")
            assert wikispecies == True
            self.clickOnElement(self.elements["_wikispecies"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Wikispecies Button")
            self.driver.back()

            self.scrollTo(self.elements["_metaWiki"]["locatorValue"], "css")
            metaWiki = self.isElementDisplayed(self.elements["_metaWiki"]["locatorValue"], "css")
            assert metaWiki == True
            self.clickOnElement(self.elements["_metaWiki"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on Meta-Wiki Button")
            self.driver.back()

            return

    def appLinks(self):
        for i in range(3):
            self.scrollTo(self.elements["_wikiAppLinks"]["locatorValue"], "css")
            wikiAppLinks = self.isElementDisplayed(self.elements["_wikiAppLinks"]["locatorValue"], "css")
            assert wikiAppLinks == True
            self.clickOnElement(self.elements["_wikiAppLinks"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on 'Download Wikipedia for Android or iOS' Link")
            self.driver.back()

            self.scrollTo(self.elements["_playStore"]["locatorValue"], "css")
            playStore = self.isElementDisplayed(self.elements["_playStore"]["locatorValue"], "css")
            assert playStore == True
            self.clickOnElement(self.elements["_playStore"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            self.windowhandling()
            self.driver.implicitly_wait(10)
            cl.allureLogs("Successfully opened and closed 'Google Play Store' page")

            self.scrollTo(self.elements["_appleStore"]["locatorValue"], "css")
            appleStore = self.isElementDisplayed(self.elements["_appleStore"]["locatorValue"], "css")
            assert appleStore == True
            self.clickOnElement(self.elements["_appleStore"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            self.windowhandling()
            self.driver.implicitly_wait(10)
            cl.allureLogs("Successfully opened and closed 'IOS Apple Store' page")

            return

    def footers(self):
        for i in range(3):
            self.scrollTo(self.elements["_license"]["locatorValue"], "css")
            license = self.isElementDisplayed(self.elements["_license"]["locatorValue"], "css")
            assert license == True
            self.clickOnElement(self.elements["_license"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on 'Creative Commons Attribution-ShareAlike License' Link")
            self.driver.back()

            self.scrollTo(self.elements["_terms"]["locatorValue"], "css")
            terms = self.isElementDisplayed(self.elements["_terms"]["locatorValue"], "css")
            assert terms == True
            self.clickOnElement(self.elements["_terms"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on 'Terms of Use' Link")
            self.driver.back()

            self.scrollTo(self.elements["_privacyPolicy"]["locatorValue"], "css")
            privacyPolicy = self.isElementDisplayed(self.elements["_privacyPolicy"]["locatorValue"], "css")
            assert privacyPolicy == True
            self.clickOnElement(self.elements["_privacyPolicy"]["locatorValue"], "css")
            self.driver.implicitly_wait(10)
            cl.allureLogs("Clicked on 'Privacy Policy' Link")
            self.driver.back()

            return

