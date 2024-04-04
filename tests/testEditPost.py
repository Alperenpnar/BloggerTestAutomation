from selenium import webdriver

from pages import LoginPages, HomePage, PostEditPage
import pytest


class TestEditPost:
    @pytest.mark.order(3)
    def testEditPost(self, setup):
        self.driver = setup
        self.driver.get("https://www.blogger.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPages.LoginPageClass(self.driver)
        self.hp = HomePage.HomePageClass(self.driver)
        self.pep = PostEditPage.PostEditPageClass(self.driver)

        # Login slenderise
        self.lp.clickSignIn()
        self.lp.inputEmail("casetest306@gmail.com")
        self.lp.clickEmailNextButton()
        self.lp.inputPassword("Asd.102030")
        self.lp.clickPasswordNextButton()
        # Edit Post

        self.pep.clickPostViewEdit()
        self.pep.textAreaPostEditPage()
        self.pep.inputTextToTextPage("Merhaba dunya")
        self.pep.DefaultFrame()
        self.pep.clickUpdateButton()
        self.pep.clickBackButton()
        self.tear_down()

    def tear_down(self):
        self.driver.close()
