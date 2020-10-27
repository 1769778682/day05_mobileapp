import time

from appium import webdriver
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.focustech.xyz'
desired_caps['appActivity'] = '.ui.main.MainActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(2)
driver.background_app(3)
time.sleep(10)
driver.quit()