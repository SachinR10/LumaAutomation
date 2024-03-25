from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture()
def setup_teardown(request):
        s = Service()
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument('incognito')
        chromeOptions.add_argument('start-maximized')
        driver = webdriver.Chrome(service=s, options=chromeOptions)
        driver.implicitly_wait(5)
        driver.get("https://magento.softwaretestingboard.com/")

        request.cls.driver = driver
        yield
        driver.close()
        driver.quit()
