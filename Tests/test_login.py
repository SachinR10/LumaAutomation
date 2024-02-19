from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Utilities.baseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.homePage import HomePage



class TestLogin(BaseClass):

    def test_login_correct_creds(self):

        homepage = HomePage(self.driver)
        signinpage = homepage.ClickSignIn()
        assert self.driver.title == "Customer Login"

        signinpage.SetUserEmail().send_keys("sachinrhumcha@gmail.com")
        signinpage.SetPassword().send_keys("Scout0p@10")
        homepage = signinpage.ClickSubmit()
        welcomeText = homepage.GetWelcomeText()

        assert welcomeText =="Welcome, Sachin R!","Login failed!"


