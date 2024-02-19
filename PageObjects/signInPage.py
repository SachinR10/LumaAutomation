from selenium.webdriver.common.by import By


class SignInPage:
    UserEmail = (By.ID,"email")
    Password = (By.ID,"pass")
    SignInButton = (By.ID,"send2")

    def __init__(self,driver):
        self.driver = driver
    
    def SetUserEmail(self):
        return self.driver.find_element(*SignInPage.UserEmail)
    
    def SetPassword(self):
        return self.driver.find_element(*SignInPage.Password)
    
    def ClickSubmit(self):
        self.driver.find_element(*SignInPage.SignInButton).click()
        #to avoid circular imports
        from PageObjects.homePage import HomePage
        return HomePage(self.driver)