import time

from appium import webdriver
# --->1.打开模拟器通讯录
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.android.contacts'
desired_caps['appActivity'] = '.activities.PeopleActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# --->2.创建一个新的联系人
driver.find_element_by_id("com.android.contacts:id/floating_action_button_container").click()
driver.find_element_by_class_name("android.widget.Button").click()
# 姓名
driver.find_element_by_xpath('//*[@text="姓名"]').send_keys("Join")
# 电话
driver.find_element_by_xpath('//*[@text="电话"]').send_keys("13812345125")
# --->3.创建完成后进入所有联系人界面
driver.find_element_by_xpath("//*[@class='android.widget.ImageButton' and @content-desc='向上导航']").click()
elem = driver.find_element_by_id("com.android.contacts:id/photo")
tel = driver.find_element_by_xpath("//*[@resource-id='com.android.contacts:id/icon' and @instance='1']")
# TouchAction(driver).move_to(elem, 600, 1000).perform()
elem.click()
driver.scroll(elem, tel)
# --->4.获取创建的联系的信息并打印
driver.find_element_by_id("com.android.contacts:id/menu_search").click()
driver.find_element_by_id("com.android.contacts:id/search_view").send_keys("Join")
print("姓名：", driver.find_element_by_xpath("//*[@text='Join']").text)
driver.find_element_by_id("com.android.contacts:id/cliv_name_textview").click()
# print(driver.find_element_by_id("com.android.contacts:id/title_gradient").text)
print("电话：", driver.find_element_by_id("com.android.contacts:id/header").text)
# --->5.删除创建的联系人
driver.find_element_by_class_name("android.widget.ImageButton").click()
driver.find_element_by_xpath("//*[@text='删除']").click()
driver.find_element_by_xpath("//*[@text='确定']").click()
time.sleep(4)
driver.quit()
