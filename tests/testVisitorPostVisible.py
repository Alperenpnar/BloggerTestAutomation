from selenium import webdriver
import pytest
from pages import VisitorPage


class TestVisitorPostVisibleClass:
    @pytest.mark.order(4)
    def testVisitorVisiblePost(self,setup):
        self.driver = setup
        self.driver.get("https://pytest12.blogspot.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.vp = VisitorPage.VisitorPageClass(self.driver)

        self.vp.postVisibleCheck()

        self.tear_down()

    def tear_down(self):
        self.driver.close()
