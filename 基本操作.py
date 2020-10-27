import time

from appium import webdriver

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.android.launcher3'
desired_caps['appActivity'] = '.Launcher'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 切换设置页面App
driver.start_activity("com.android.settings", ".Settings")
title = driver.find_element_by_xpath(
    "//*[@resource-id='com.android.settings:id/title' and @instance='3']")
print(title)
# 打印WLAN的位置
loc = title.location
print(loc)
# 打印WLAN的大小
size = title.size
print(size)
time.sleep(4)
driver.quit()
