import time
import pytest
from selenium import webdriver

from pages import VisitorPage, LoginPages


class TestAddCommentVisitor:
    @pytest.mark.order(5)
    def testAddCommentVisitor(self,setup):
        self.driver = setup
        self.driver.get("https://pytest12.blogspot.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPages.LoginPageClass(self.driver)
        #Post Visible check
        self.vp = VisitorPage.VisitorPageClass(self.driver)
        self.vp.postVisibleCheck()
        #Post add commnet and Sing In
        self.vp.clickPostACommentButton()
        self.vp.swicthToIframeForSingInWithGoogle()
        self.vp.clickToSingInGoogleButton()
        #Giris bilgileri
        self.lp.inputEmail("visitortest7@gmail.com")
        self.lp.clickEmailNextButton()
        self.lp.inputPassword("Asd.102030")
        self.lp.clickPasswordNextButton()
        time.sleep(3)
        #Add comment
        self.vp.swicthToIframeForCommentTextArea()
        self.vp.inputCommentTextArea()
        self.vp.clickCommentPublishButton()
        time.sleep(2)

        self.tear_down()

    def tear_down(self):
        self.driver.close()



