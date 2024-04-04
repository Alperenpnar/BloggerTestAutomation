import time

from selenium.webdriver.common.by import By


class HomePageClass:
    homePageTitle = "Blogger: Posts"
    NewPostAddButtonXpath = "//div[@class='SpTCHb']//span[@class='MIJMVe'][normalize-space()='New Post']"
    CommentButtonCss = "c-wiz[class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e'] span[aria-label='Comments'] div[class='kurlme DQGx6d']"
    homePageCheckCss = "a[id='sdgBod'] img[role='presentation']"
    buttonPostXpath = "a[href='./blog/posts/2141914943888917403']"
    def __init__(self, driver):
        self.driver = driver

    def homePageCheck(self):
        if self.driver.find_element(By.CSS_SELECTOR, self.homePageCheckCss):
            return True
        else:
            return False

    def clickNewPostAddButton(self):
        self.driver.find_element(By.XPATH, self.NewPostAddButtonXpath).click()
        time.sleep(3)

    def clickCommentButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.CommentButtonCss).click()

    def clickPostButton(self):
        self.driver.find_element(By.XPATH,self.buttonPostXpath).click()