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

class TestBlogshop():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_blogshop(self):
    # Test name: blog_shop
    # Step # | name | target | value
    # 1 | open | https://homedeco276986908.wordpress.com/ | 
    self.driver.get("https://homedeco276986908.wordpress.com/")
    # 2 | setWindowSize | 1936x1056 | 
    self.driver.set_window_size(1936, 1056)
    # 3 | runScript | window.scrollTo(0,2415) | 
    self.driver.execute_script("window.scrollTo(0,2415)")
    # 4 | click | linkText=Shop Sweet Shop | 
    self.driver.find_element(By.LINK_TEXT, "Shop Sweet Shop").click()
    assert "No results found." not in self.driver.page_source
  