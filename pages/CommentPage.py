import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages import VisitorPage


class CommentPageClass:
    vp = VisitorPage.VisitorPageClass
    # Locators
    commentClassName = "LgQiCc"
    fieldCommentDeleteXpath = "(//div[@class='opmHNc'])[1]"
    deleteCommentIconXpath = "//*[@id='yDmH0d']/c-wiz[2]/div[2]/div/c-wiz/div[2]/c-wiz/div/div/div/div/span/div/div/div[4]/div[3]/span/span/span"
    clickCommentDeleteButtonXpath = "//*[@id='yDmH0d']/div[4]/div/div[2]/div[2]/div[2]"
    viewCommentsXpath = "//li[@class='comment']"
    visitorPageCheckCss = "a[href='https://www.blogger.com']"
    commentId = "8011379938220052200"
    commentListItemsCSS = "div[class='LgQiCc vOSR6b']"

    def __init__(self, driver):
        self.driver = driver

    def commentVisibleCheck(self):
        elements = self.driver.find_elements(By.CLASS_NAME, self.commentClassName)
        if not elements:
            return False
        else:
            return True

    def fieldCommentDeleteButton(self):
        action = ActionChains(self.driver)
        deleteItemList = self.driver.find_element(By.XPATH, self.fieldCommentDeleteXpath)
        action.move_to_element(deleteItemList).perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.deleteCommentIconXpath).click()

    def clickCommentDeleteButton(self):
        self.driver.find_element(By.XPATH, self.clickCommentDeleteButtonXpath).click()
        time.sleep(2)

    def checkCommentDelete(self):
        comments = self.driver.find_element(By.XPATH, self.viewCommentsXpath)

        for comment in comments:
            currentCommentId = comment.get.attribute("data-commentid")
            print(currentCommentId)
            if currentCommentId == self.commentId:
                return False

        return True

    def commentNumber(self):  # Kullanılacak!!!!

        commentList = self.driver.find_elements(By.CSS_SELECTOR, self.commentListItemsCSS)
        if not commentList:
            commentNum = 0
        else:
            commentNum = len(commentList)
            # Config.total_comment_number = len(comment_list)
        return commentNum