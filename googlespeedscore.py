# from selenium import webdriver
# import unittest
# import time
# from selenium.webdriver.common.keys import Keys
#
#
# driver = webdriver.Chrome(executable_path='/home/chinmayaggarwal/PycharmProjects/appiumsandbox/Driver/chromedriver')
# driver.maximize_window()
# driver.get("https://www.renewbuy.com")
# lnks=driver.find_elements_by_tag_name("a")
# l=[]
# for lnk in lnks:
#
#     val=lnk.get_attribute("href")
#     l.append(val)
# print(l)
#
#
# count=0
# for i in l:
#     if i==None:
#         print(count)
#     # elif(l[0]!=None):
#     #     print(count)
#     else:
#         print("count is not none",count)
#         count=count+1
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # driver.quit()
#
#
#
# #
# # driver.get("https://developers.google.com/speed/pagespeed/insights/?hl=de")
# # # driver.find_element_by_xpath('//*[@id="page-speed-insights"]/div[1]/form/div/input').send_keys('Renewbuy.com')
# # # driver.find_element_by_xpath('//*[@id="page-speed-insights"]/div[1]/form/div/div/div').submit()
# # # driver.find_element_by_xpath('//*[@id=":8"]').click()
# # i=["google",'iioo']
# # li=[i for i in range(50)]
# # print(i)
# # number=['india','iis']
# # list=[num[0]for num in number]
# # print(list)
# # l=[1,2,1,4]
# # count=0
# # for i in range(4):
# #     if l[i]!=1:
# #         count=count+1
# #        k
# #     else:
# #         print(i)
#
#
#
#
#
#
#
#
#
# #search.click()
# # print(driver.title
# # search_bar = driver.find_element_by_name("q")
# # search_bar.clear()
# # search_bar.send_keys("getting started with python")
# # search_bar.send_keys(Keys.RETURN)
# # print(driver.current_url)
# # driver.close()
#
# # l=[2,3,5,6,7]
# # for i in l:
# #     print(i)
#
# # import requests
# #
# # # Making a POST request
# # r = requests.get('https://httpbin.org /')
# #
# # # check status code for response recieved
# # # success code - 200
# # print(r)
#
# # print content of request

import unittest

class TestStringMethod():

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
