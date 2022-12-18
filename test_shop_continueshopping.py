# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestContinueShopping():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_continueshopping(self):
        # Test name: shop2
        # open product page in shop
        self.driver.get("https://63580b0bc4fa9.site123.me//shop-1/white-ceramic-plate")
        # find the add to cart button
        self.driver.find_element(By.XPATH, "(//*[contains(text(),'Add To Cart')])[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="cartOrderPage"]/div/div[2]/div[1]/div[2]/div[2]/div[2]/a').click()
        shop_page = self.driver.find_element(By.XPATH, '//*[@id="section-112"]/div[3]/div[2]/div/div[1]/h3')
        shop_page_title = shop_page.get_attribute('innerText')
        assert "Related products" in shop_page_title


