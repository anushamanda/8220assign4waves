import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class AAF_Test3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_logout(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://ofws.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[2]/a').click()
        time.sleep(0.5)
        elem = driver.find_element_by_id("username")
        elem.send_keys("instructor")
        elem = driver.find_element_by_id("password")
        elem.send_keys("maverick1a")
        elem = driver.find_element_by_xpath('//*[@id="login"]/div/div/div/div/div[2]/form/input[2]').click()
        time.sleep(1.5)

        try:
            # attempt to find the plus button - if found, logged in
            time.sleep(1.5)
            elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/li[2]/a')
            logout = True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

        if logout:
            elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/li[3]/ul/li[1]/a').click()
            time.sleep(1.5)
            try:
               # find the 'edit' pencil icon - if post added, edit pate is displayed
               elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[2]/a')
               assert True
               time.sleep(1.5)
            except NoSuchElementException:
                self.fail("Logout not successfull")
                assert False
                time.sleep(0.5)

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()