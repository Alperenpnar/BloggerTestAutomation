import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class PostPageClass:
    # Locators
    viewPostCss = "a[href='./blog/post/edit/2141914943888917403/2138616735968021837']"
    postItemXpath = "//*[@id='yDmH0d']/c-wiz/div[2]/div/c-wiz/div[2]/c-wiz/div/div/div/div[1]/div"
    postItemDeleteIconXpath = "(//span[@class='DPvwYc'][contains(text(),'')])[2]"
    postItemDeleteButtonXpath = "(//span[@class='RveJvd snByac'][normalize-space()='Trash post'])[2]"
    postCountClass = "yGrhUb"

    def __init__(self, driver):
        self.driver = driver

    def clickPostViewArea(self):
        self.driver.find_element(By.CSS_SELECTOR, self.viewPostCss).click()

    def clickPostDeleteIcon(self):
        action = ActionChains(self.driver)
        PostItemList = self.driver.find_element(By.XPATH, self.postItemXpath)
        action.move_to_element(PostItemList).perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.postItemDeleteIconXpath).click()

    def clickPostDeleteButton(self):
        self.driver.find_element(By.XPATH, self.postItemDeleteButtonXpath).click()
        time.sleep(2)

    def checkPostDelete(self):
        postList = self.driver.find_elements(By.CLASS_NAME, self.postCountClass)
        if not postList:
            postNumber = 0
        else:
            postNumber = len(postList)
        print(postNumber)
        if postNumber <= 1:
            return True
        else:
            return False
