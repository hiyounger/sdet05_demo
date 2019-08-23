import unittest

from selenium import webdriver
from Yzx.templates_example.page_is_opean_judage.juage import Juage

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_case01_something(self):
        juage = Juage(self.driver)
        juage.open()
        ret_statu, ret_msg = juage.if_page_opened_success()
        # print("exp:%s, act:%s" % (ret_msg['title']['exp_value'], ret_msg['title']['act_value']))
        self.assertEqual(True, ret_statu, str(ret_msg))

if __name__ == '__main__':
    unittest.main()
