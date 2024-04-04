from pages import PostEditPage, HomePage, LoginPages, CommentPage
from selenium import webdriver
from pages import LoginPages, HomePage, CommentPage
import pytest


class TestCheckAndDeleteCommentClass:

    @pytest.mark.order(6)
    def testCheckCommentAndDelete(self, setup):
        self.driver = setup
        self.driver.get("https://www.blogger.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPages.LoginPageClass(self.driver)
        self.hp = HomePage.HomePageClass(self.driver)
        self.cp = CommentPage.CommentPageClass(self.driver)
        # Sing In by Admin
        self.lp.clickSignIn()
        self.lp.inputEmail("casetest306@gmail.com")
        self.lp.clickEmailNextButton()
        self.lp.inputPassword("Asd.102030")
        self.lp.clickPasswordNextButton()

        # Click comment Button
        self.hp.clickCommentButton()

        self.cp.commentVisibleCheck()
        # COMMETN sayisini tut
        preCommentNumber = self.cp.commentNumber()

        self.cp.fieldCommentDeleteButton()
        self.cp.clickCommentDeleteButton()
        afterCommentNumber = self.cp.commentNumber()
        print(preCommentNumber, "  vs ", afterCommentNumber)

        if preCommentNumber - afterCommentNumber == 1:
            assert True

        else:
            assert False

        self.tearDown()

    def tearDown(self):
        self.driver.close()
