# -*- coding: utf-8 -*-

from selenium import  webdriver
import unittest


def setProxy():
    profile=webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type",1)
    profile.set_preference("network.proxy.http","135.245.192.6")
    profile.set_preference("network.proxy.http_port",8000)
    profile.update_preferences()

    return profile

class NewVisitorTest(unittest.TestCase):
    def setUp(self):  #
        profile=setProxy()
        self.browser = webdriver.Firefox(firefox_profile=profile)
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)  #
        self.fail('Finish the test!')

if __name__ == '__main__':  #
    unittest.main(warnings='ignore')