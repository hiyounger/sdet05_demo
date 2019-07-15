#encoding:utf-8

import unittest
from selenium import webdriver
from Rand10Page import Rand10Page


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_case01_something(self):
        rand10sec_page = Rand10Page(self.driver)
        rand10sec_page.open()
        ret_statu, ret_msg = rand10sec_page.if_page_opened_success()
        self.assertEqual(True, ret_statu, str(ret_msg))

if __name__ == '__main__':
    unittest.main()
