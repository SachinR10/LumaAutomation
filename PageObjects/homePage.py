from selenium.webdriver.common.by import By

import time

class HomePage:
    SignInLink = (By.XPATH,"//div[@class='panel header']//li[@class='authorization-link']//*[contains(text(),'Sign In')]")
    WelcomeXpath = (By.XPATH,"//div[@class='panel header']//li[@class='greet welcome']")

    def __init__(self,driver):
        self.driver = driver
    
    def ClickSignIn(self):
        self.driver.find_element(*HomePage.SignInLink).click()
        #to avoid circular imports
        from PageObjects.signInPage import SignInPage
        return SignInPage(self.driver)

    def GetWelcomeText(self):
        time.sleep(3)
        return self.driver.find_element(*HomePage.WelcomeXpath).text
