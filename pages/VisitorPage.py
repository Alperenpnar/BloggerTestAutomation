import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#sahdgsjahg

class VisitorPageClass:
    # Locatorlar
    noPostMessageCSS = "div[class='no-posts-message']"
    postFeaturedID = "FeaturedPost1"
    postCommentCSS = "span[class='num_comments']"
    iframeCommentNAME = "comment-editor"
    googleSignInCSS = "div[aria-label='Sign in with Google'] span[class='RveJvd snByac']"
    commentTextAreaXpath = "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/div[2]/div[2]/div[1]/div[2]/textarea"
    commentTextAreaCSS = "textarea[aria-label='Enter Comment']"
    publishCommentButtonCSS = "div[aria-label='Publish'] span[class='RveJvd snByac']"
    publishedCommentCSS = ".comment-content"

    CommentNumberCSS = "span[class='num_comments']"
    visitorPageUrl = "https://pytest12.blogspot.com/"
    postTitle = "#Header1 > div > div > h1"
    commentText = "sahane!!"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Post visible check
    def postVisibleCheck(self):
        try:
           # self.driver.find_element(By.CSS_SELECTOR, self.postFeaturedID)
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.postFeaturedID)))
            if element.is_displayed():
                assert True
            else:
                assert False
            print("Post element found.")
        except NoSuchElementException:
            print("Post element not found.")

    time.sleep(3)

    # Visitor Post Add Comment

    def clickPostACommentButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.postCommentCSS).click()
        time.sleep(2)

    def swicthToIframeForSingInWithGoogle(self):
        """Switch to post iframe"""
        time.sleep(1)
        iframe = self.driver.find_element(By.NAME, "comment-editor")
        self.driver.switch_to.frame(iframe)
        time.sleep(3)

    def clickToSingInGoogleButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.googleSignInCSS).click()
        time.sleep(3)
    def swicthToIframeForCommentTextArea(self):
        iframe = self.driver.find_element(By.NAME, "comment-editor")
        self.driver.switch_to.frame(iframe)


    def inputCommentTextArea(self):
        self.driver.find_element(By.CSS_SELECTOR, self.commentTextAreaCSS).send_keys(self.commentText)
        time.sleep(2)

    def clickCommentPublishButton(self):
        self.driver.find_element(By.CSS_SELECTOR,self.publishCommentButtonCSS).click()

    def CommentCheckAfterDeletion(self):
        CommentText = self.driver.find_element(By.CSS_SELECTOR, self.CommentNumberCSS).text
        if "Post" in CommentText:
            print("yorum yok")
            assert True
        else:
            text_parts = CommentText.split(" comment")
            commentNumber = text_parts[0]
            print(commentNumber)
            assert False



