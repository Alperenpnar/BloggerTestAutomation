from selenium import webdriver
import pytest
from pages import LoginPages, HomePage, PostEditPage


# https://r.resimlink.com/XyJWfFQL7N0.png

class TestNewPost:
    @pytest.mark.order(2)
    def testAddNewPost(self,setup):
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

        # Yeni post ekleme islemleri
        self.hp.clickNewPostAddButton()

        # post image yukleme islemleri
        self.pep.clickInsertImageButton()
        self.pep.clickByUrlButton()
        self.pep.inputUrlTextBox("https://r.resimlink.com/ER-mHvC53iK.png")
        self.pep.clickSelectButton()
        self.pep.clickPublishButton()
        self.pep.clickConfirmButton()

        self.tear_down()

    def tear_down(self):
        self.driver.close()