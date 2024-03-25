from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Utilities.baseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.homePage import HomePage
from Utilities.logGen import LogGen


class TestLogin(BaseClass):
    logger = LogGen.loggen()

    def test_login_correct_creds(self):
        self.logger.info("strated TS- Login with correct creds")
        homepage = HomePage(self.driver)
        signinpage = homepage.ClickSignIn()
        assert self.driver.title == "Customer Login"

        signinpage.SetUserEmail().send_keys("sachinrhumcha@gmail.com")
        signinpage.SetPassword().send_keys("Scout0p@10")
        signinpage.ClickSubmit()
        homepage = HomePage(self.driver)
        welcomeText = homepage.GetWelcomeText()

        assert welcomeText =="Welcome, Sachin R!","Login failed!"


    def test_login_incorrect_creds(self):
        self.logger.info("strated TS- Login with incorrect creds")
        homePage = HomePage(self.driver)
        SignInPage = homePage.ClickSignIn()
        assert self.driver.title == "Customer Login"

        SignInPage.SetUserEmail().send_keys("seafdffdf@gmail.com")
        SignInPage.SetPassword().send_keys("ScoutOp@10")
        SignInPage.ClickSubmit()

        assert self.driver.title == "Customer Login"
        assert SignInPage.getAlertText() == "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."





    


    


