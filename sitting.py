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
# 通过id定位进行点击事件。点击设置中的搜索图标
driver.find_element_by_id("com.android.settings:id/search").click()
# 通过class属性进行输入
driver.find_element_by_class_name("android.widget.EditText").send_keys("hello")
time.sleep(2)
# 通过Xpath定位元素。输入后返回
driver.find_element_by_xpath("//*[@class='android.widget.ImageButton']").click()
time.sleep(2)
# 通过Xpath定位点击蓝牙
driver.find_element_by_xpath("//*[@text='蓝牙']").click()
time.sleep(4)
driver.quit()