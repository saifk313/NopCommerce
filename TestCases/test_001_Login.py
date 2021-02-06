import pytest
from selenium import webdriver

from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ConfigReader
from Utilities.customLogger import LogGen


class TestLogin:
    base_url = ConfigReader.getUrl()
    username = ConfigReader.getUserEmail()
    password = ConfigReader.getPassword()

    logger = LogGen.logGen()

    def test_homePageTitle(self, setup):
        self.logger.info("************** test_homePageTitle **************")
        self.driver = setup
        self.logger.info("************** Started Home Page Title Test **************")
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        if actual_title == "Your store. Login123":
            assert True
            self.driver.close()
            self.logger.info("### Home Page Title Test Passed ###")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_title.png")
            self.driver.close()
            self.logger.error("### Home Page Title Test Failed ###")
            assert False

    def test_002_login(self, setup):
        self.logger.info("************** test_002_login **************")
        self.driver = setup
        self.logger.info("************** Started Login Test **************")
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)
        self.login.setUsername(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("### Login Test Passed ###")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            self.driver.close()
            self.logger.error("### Login Test Failed ###")
            assert False
