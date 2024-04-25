from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pages import LoginPages
from pages.LoginPages import LoginPageClass
import pytest

class TestPage:

    @pytest.mark.order(1)
    def testLogin(self,setup):

        self.driver = setup
        self.driver.get("https://www.blogger.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = LoginPages.LoginPageClass(self.driver)


        self.lp.clickSignIn()
        self.lp.inputEmail("casetest306@gmail.com")
        self.lp.clickEmailNextButton()
        self.lp.inputPassword("Asd.102030")
        self.lp.clickPasswordNextButton()

        self.tear_down()

    def tear_down(self):
        self.driver.close()
