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

class TestShareontwitter():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_shareontwitter(self):
    # Test name: shareontwitter
    # Step # | name | target | value
    # 1 | open | https://homedeco276986908.wordpress.com/ | 
    self.driver.get("https://homedeco276986908.wordpress.com/")
    # 2 | setWindowSize | 1936x1056 | 
    self.driver.set_window_size(1936, 1056)
    # 3 | click | linkText=Blog | 
    self.driver.find_element(By.LINK_TEXT, "Blog").click()
    # 4 | click | linkText=Tips for Autumnal Decor |
    self.vars["window_handles"] = self.driver.window_handles
    # 5 | selectWindow | handle=${win9197} |
    self.driver.find_element(By.LINK_TEXT, "Tips for Autumnal Decor").click()
    # 6 | runScript | window.scrollTo(0,4500) |
    self.vars["win9197"] = self.wait_for_window(2000)
    # 7 | click | css=.share-twitter > span |
    self.driver.switch_to.window(self.vars["win9197"])
    # 8 | selectWindow | handle=${win6289} |
    self.driver.execute_script("window.scrollTo(0,6500)")
    time.sleep(5)
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".share-twitter > span").click()
    self.vars["win6289"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win6289"])
    assert "Page not found." not in self.driver.page_source