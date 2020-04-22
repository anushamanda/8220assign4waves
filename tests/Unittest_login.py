import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class AAF_Test2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://ofws.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[2]/a').click()
        time.sleep(0.5)
        elem = driver.find_element_by_id("username")
        elem.send_keys("instructor")
        elem = driver.find_element_by_id("password2")
        elem.send_keys("maverick1a")
        elem = driver.find_element_by_xpath('//*[@id="login"]/div/div/div/div/div[2]/form/input[2]').click()
        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/li[2]/a')
            assert True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
