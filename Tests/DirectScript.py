from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


s = Service()

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('incognito')
chromeOptions.add_argument('start-maximized')


driver = webdriver.Chrome(service=s, options=chromeOptions)
driver.implicitly_wait(5)


driver.get("https://magento.softwaretestingboard.com/")

driver.find_element(By.XPATH,"//div[@class='panel header']//li[@class='authorization-link']//*[contains(text(),'Sign In')]").click()

assert driver.title == "Customer Login"

driver.find_element(By.ID,"email").send_keys("sachinrhumcha@gmail.com")
driver.find_element(By.ID,"pass").send_keys("Scout0p@10")
driver.find_element(By.ID,"send2").click()

time.sleep(3)

#//div[@class='page messages']

driver.close()
driver.quit()

