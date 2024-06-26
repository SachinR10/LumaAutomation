from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Utilities.baseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.homePage import HomePage
from Utilities.logModule import LogModule
from Utilities.readJSON import ReadJson
import pytest

class TestLogin(BaseClass):
    logger = LogModule.get_logger("TestLogin")

    def test_login_correct_creds(self):
        self.logger.info("strated TS- Login with correct creds")
        homepage = HomePage(self.driver)
        signinpage = homepage.ClickSignIn()
        if self.driver.title == "Customer Login":
            self.logger.info("Entered Customer Login Page")
        else:
            self.logger.error("Failed to enter Custom Login Page, Current Page title = %s", self.driver.title)
            assert False
        LoginCorrectCreds = ReadJson('D:/Projects/LumaAutomation/Data/LoginCorrectCreds.json')
        signinpage.SetUserEmail().send_keys(LoginCorrectCreds.getData("Email"))
        signinpage.SetPassword().send_keys(LoginCorrectCreds.getData("Password"))
        signinpage.ClickSubmit()
        homepage = HomePage(self.driver)
        welcomeText = homepage.GetWelcomeText()

        if welcomeText =="Welcome, Sachin R!" :
            self.logger.info("Login with correct creds success")
            assert True
        else:
            self.logger.error("Login with correct creds failed")
            assert False

    
    def test_login_incorrect_creds(self):
        self.logger.info("strated TS- Login with incorrect creds")
        homePage = HomePage(self.driver)
        SignInPage = homePage.ClickSignIn()
        if self.driver.title == "Customer Login":
            self.logger.info("Entered Custom Login Page")
        else:
            self.logger.error("Failed to enter Custom Login Page, Current Page title = %s", self.driver.title)
        
        
        LoginIncorrectCreds = ReadJson('D:/Projects/LumaAutomation/Data/LoginIncorrectCreds.json')
        
        
        SignInPage.SetUserEmail().send_keys(LoginIncorrectCreds.getData("Email"))
        SignInPage.SetPassword().send_keys(LoginIncorrectCreds.getData("Password"))
        SignInPage.ClickSubmit()

        if self.driver.title == "Customer Login":
            self.logger.info("Still in Custome Login Page When incorrect creads entered")
            assert True
        else:
            self.logger.error("Whent to %s when incorrect creds entered",self.driver.title)
            assert False
        PopUpMessage = SignInPage.getAlertText()
        if PopUpMessage == "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.":
            self.logger.info("Correct Pop up message appeared")
            assert True
        else:
            self.logger.error("Incorrect Pop-Up message appeared Actual=%s",PopUpMessage)





    


    


