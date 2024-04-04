from pages import LoginPages, HomePage, PostEditPage, CommentPage, VisitorPage
import pytest
@pytest.mark.order(7)
class TestVisitorCheckDeleteComment:



    def testVisitorCheckDeleteComment(self,setup):
        self.driver = setup
        self.driver.get("https://pytest12.blogspot.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)



        self.vp = VisitorPage.VisitorPageClass(self.driver)
        self.vp.postVisibleCheck()
        self.vp.CommentCheckAfterDeletion()

        self.tear_down()

    def tear_down(self):
        self.driver.close()










