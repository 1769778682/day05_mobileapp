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
driver.close_app()

if driver.is_app_installed("com.itcast.toutiaoApp"):
    driver.remove_app("com.itcast.toutiaoApp")
    driver.install_app(r"C:\Users\sandysong\Desktop\pagetest\HeimaToutiao_v0.6_build2019031101.apk")
else:
    driver.install_app(r"C:\Users\sandysong\Desktop\pagetest\HeimaToutiao_v0.6_build2019031101.apk")
# time.sleep(2)
# print("包名是：", driver.current_package, "\n" "界面名是：", driver.current_activity)
time.sleep(4)
driver.quit()