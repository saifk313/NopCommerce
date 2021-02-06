import pytest
from selenium import webdriver
import time

from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ConfigReader
from Utilities.customLogger import LogGen
from Utilities import ExcelUtils


class TestLogin:
    base_url = ConfigReader.getUrl()
    logger = LogGen.logGen()
    path = "./TestData/TestData.xlsx"
    sheet = "Sheet1"

    def test_DDT_login(self, setup):
        self.logger.info("************** test_002_DDT_login **************")
        self.driver = setup
        self.logger.info("************** Started Login Test **************")
        self.driver.get(self.base_url)
        self.login = LoginPage(self.driver)

        self.rows = ExcelUtils.getRows(self.path, "Sheet1")
        print(self.rows)

        lst_status = []

        for row in range(2, self.rows + 1):
            print("Started Iteration:", row - 1)
            self.user = ExcelUtils.readData(self.path, self.sheet, row, 1)
            self.pwd = ExcelUtils.readData(self.path, self.sheet, row, 2)
            self.expected_result = ExcelUtils.readData(self.path, self.sheet, row, 3)

            self.login.setUsername(self.user)
            self.login.setPassword(self.pwd)
            self.login.clickLogin()

            time.sleep(3)

            expected_title = "Dashboard / nopCommerce administration"
            actual_title = self.driver.title

            if actual_title == expected_title:
                if self.expected_result == "Pass":
                    lst_status.append("Pass")
                    self.logger.info("*** Passed ***")
                    self.login.clickLogout()
                    # assert True
                elif self.expected_result == "Fail":
                    lst_status.append("Fail")
                    self.logger.info("*** Failed ***")
                    self.login.clickLogout()
                    # assert False
            elif actual_title != expected_title:
                if self.expected_result == "Fail":
                    lst_status.append("Pass")
                    self.logger.info("*** Passed ***")
                    # assert True
                elif self.expected_result == "Pass":
                    lst_status.append("Fail")
                    self.logger.info("*** Failed ***")
                    # assert False
            print("Completed Iteration:", row - 1)

        if "Fail" not in lst_status:
            self.logger.info("##### Test Case Passed ######")
            assert True
        else:
            self.logger.info("##### Test Case Failed #####")
            assert False
        self.driver.close()
        self.logger.info("******** End of DDT Login Test ***********")
        self.logger.info("******** Completed DDT Login Test ***********")
