import unittest

from selenium import webdriver
from rand10sec_page import Rand10SecPage,Webdriver_Demo

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_case01_something(self):
        rand10sec_page = Rand10SecPage(self.driver)
        rand10sec_page.open()
        ret_statu, ret_msg = rand10sec_page.if_page_opened_success()
        self.assertEqual(True, ret_statu, str(ret_msg))

    def test_case02_something(self):
        webdriver_demo = Webdriver_Demo(self.driver)
        webdriver_demo.open()
        ret_statu, ret_msg = webdriver_demo.if_page_opened_success()
        self.assertEqual(True, ret_statu, str(ret_msg))


if __name__ == '__main__':
    unittest.main()
