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
# 点击放大镜搜索图标
driver.find_element_by_id("com.android.settings:id/search").click()
# 输入hello
driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
# 清除文本
driver.find_element_by_id("android:id/search_src_text").clear()
# 点击返回主页
driver.find_element_by_class_name("android.widget.ImageButton").click()
# 获取WLAN文本信息
title = driver.find_element_by_xpath(
    "//*[@resource-id='com.android.settings:id/title' and @instance='3']").text
print(title)
time.sleep(4)
driver.quit()