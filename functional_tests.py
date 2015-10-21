# -*- coding: utf-8 -*-

from selenium import  webdriver



profile=webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type",1)
profile.set_preference("network.proxy.http","135.245.192.6")
profile.set_preference("network.proxy.http_port",8000)

profile.update_preferences()

browser=webdriver.Firefox(firefox_profile=profile)
browser.get('http://127.0.0.1:8000')
#browser.get('http://www.baidu.com')
assert 'Django' in browser.title

