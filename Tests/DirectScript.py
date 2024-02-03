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

print(driver.title)

time.sleep(3)


driver.close()
driver.quit()

