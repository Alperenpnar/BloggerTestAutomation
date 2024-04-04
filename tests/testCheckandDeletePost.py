from pages import LoginPages, PostPage, VisitorPage
import pytest


@pytest.mark.order(8)
class TestCheckAndDeletePost:

    def testCheckAndDeletePost(self, setup):
        self.driver = setup
        self.driver.get("https://www.blogger.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = LoginPages.LoginPageClass(self.driver)
        self.pp = PostPage.PostPageClass(self.driver)
        self.vp = VisitorPage.VisitorPageClass(self.driver)
        # Admin girisi
        self.lp.clickSignIn()
        self.lp.inputEmail("casetest306@gmail.com")
        self.lp.clickEmailNextButton()
        self.lp.inputPassword("Asd.102030")
        self.lp.clickPasswordNextButton()

       # assert self.vp.postVisibleCheck()
        # Post Delete process

        self.pp.clickPostDeleteIcon()
        self.pp.clickPostDeleteButton()
        self.pp.checkPostDelete()


        self.tear_down()

    def tear_down(self):
        self.driver.close()