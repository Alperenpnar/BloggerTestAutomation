import time

import pyperclip
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class PostEditPageClass:
    insertImageButtonXpath = "(//span[contains(@class,'DPvwYc sm8sCf GHpiyd')][contains(text(),'')])[1]"
    insertUrlLinkButtonCss = "div[class='JPdR6b e5Emjc qjTEB'] span[aria-label='By URL']"
    inputUrlTextBoxCss = "input[id=':c']"
    selectButtonId = "picker:ap:0"
    publishButtonCss = "div[aria-label='Publish'] span[class='CwaK9']"
    confirmButtonXpath = "/html[1]/body[1]/div[7]/div[4]/div[1]/div[2]/div[3]/div[2]/span[1]/span[1]"
    # ------------------------------------------------------------------------------------------------
    #clickPostViewEditCss = "a[href='./blog/post/edit/2141914943888917403/2138616735968021837']"
    postPublishedXpath = "//c-wiz[@class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e']//a[@class='azat BJi0D']"
    textBoxViewClickXpath = "(//body)[1]"
    iframePageButtonCss = "iframe[class='ZW3ZFc editable']"
    clickUpdateButtonCss = "div[aria-label='Update'] div[class='A2yzVd']"
    clickButtonBackCss = "div[title='Go back']"

    def __init__(self, driver):
        self.driver = driver

    # New Post And Image Download
    def clickInsertImageButton(self):
        self.driver.find_element(By.XPATH, self.insertImageButtonXpath).click()
        time.sleep(3)

    def clickByUrlButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.insertUrlLinkButtonCss).click()

    def inputUrlTextBox(self, url):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "/html/body/div[11]/div[2]/div/iframe"))
        textBoxUrl = self.driver.find_element(By.CSS_SELECTOR, self.inputUrlTextBoxCss)
        pyperclip.copy(url)
        textBoxUrl.send_keys(Keys.CONTROL, 'v')
        time.sleep(5)

    def clickSelectButton(self):
        self.driver.find_element(By.ID, self.selectButtonId).click()
        time.sleep(3)

    def clickPublishButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.publishButtonCss).click()
        time.sleep(3)

    def clickConfirmButton(self):
        self.driver.find_element(By.XPATH, self.confirmButtonXpath).click()
        time.sleep(3)

    # Post Edit Process

    def clickPostViewEdit(self):
        self.driver.find_element(By.XPATH, self.postPublishedXpath).click()
        time.sleep(3)


    def textAreaPostEditPage(self):
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "iframe[class='ZW3ZFc editable']"))
        time.sleep(3)

    def inputTextToTextPage(self, text):
        pyperclip.copy(text)
        self.driver.find_element(By.XPATH, self.textBoxViewClickXpath).send_keys(Keys.CONTROL, 'v')
        time.sleep(3)

    def DefaultFrame(self):
        self.driver.switch_to.default_content()

    def clickUpdateButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.clickUpdateButtonCss).click()
        time.sleep(2)

    def clickBackButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.clickButtonBackCss).click()
        time.sleep(3)
