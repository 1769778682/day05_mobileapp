import time

from appium import webdriver
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(2)
# 通过 id 的形式，获取所有 resource-id 为 ”com.android.settings:id/title“ 的元素，
# 并打印其文字内容
title = driver.find_elements_by_id("com.android.settings:id/title")
for i in range(len(title)):
    print(title[i].text)

print("-" * 30)
# 通过 class_name 的形式，获取所有class 为 ”android.widget.TextView“ 的元素，
# 并打印其文字内容
class_name = driver.find_elements_by_class_name("android.widget.TextView")
for i in range(len(class_name)):
    print(class_name[i].text)
print("-" * 30)
# 通过 xpath 的形式，获取所有包含 ”设“ 的元素，
# 并打印其文字内容
contains = driver.find_elements_by_xpath("//*[contains(@text,'设')]")
for i in range(len(contains)):
    print(contains[i].text)
time.sleep(4)
driver.quit()