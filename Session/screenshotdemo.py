import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_cap={

  "platformName": "Android",
  "deviceName": "Android Emulator",
  "app": "/home/chinmayaggarwal/Downloads/app-main1-x86-release.apk",
  "newCommandTimeout": "30000"

}

driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

driver.implicitly_wait(10)

# TouchAction(driver)   .press(x=131, y=2642)   .move_to(x=226, y=2654)   .release()   .perform()
for i in range(4):
  touch=TouchAction(driver)
  touch.press(x=1321, y=2666).move_to(x=1309, y=2707).release().perform()
  ts = time.strftime("%y_%m_%d_%H_%M_%S_")
  activity_name = driver.current_activity
  filename = activity_name + ts
  driver.save_screenshot("/home/chinmayaggarwal/PycharmProjects/appiumsandbox/screenshot" + filename + ".png")

emailid=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText')
emailid.send_keys('nitesh.aswal22@gmail.com')
password=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.EditText')
password.send_keys('Test@123')
submit=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]')
submit.click()
ts=time.strftime("%y_%m_%d_%H_%M_%S_")
activity_name=driver.current_activity
filename=activity_name+ts
driver.save_screenshot("/home/chinmayaggarwal/PycharmProjects/appiumsandbox/screenshot"+filename+".png")
