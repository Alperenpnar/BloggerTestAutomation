from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class LoginPageClass:
    signInButtonTagName = "span"
    emailTextBoxId = "identifierId"
    emailNextButtonCss = "#identifierNext > div > button > span"
    passwordTextBoxCss = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"
    passwordNextButtonCss = "#passwordNext > div > button > span"

    def __init__(self,driver):
        self.driver = driver


    def clickSignIn(self):
        self.driver.find_element(By.TAG_NAME,"span").click()

    def inputEmail(self, email):
        self.driver.find_element(By.ID, self.emailTextBoxId).send_keys(email)
        time.sleep(2)

    def clickEmailNextButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.emailNextButtonCss).click()
        time.sleep(2)

    def inputPassword(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.passwordTextBoxCss).send_keys(password)
        time.sleep(2)

    def clickPasswordNextButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.passwordNextButtonCss).click()
        time.sleep(2)

