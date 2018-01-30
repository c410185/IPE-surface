# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from time import clock

chromedriver = 'C:\\Users\何方辉\AppData\Local\Google\Chrome\Application\chromedriver.exe'

options = webdriver.ChromeOptions()
#options.add_argument('headless')
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': 'C:\DTLDownLoads\\'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
driver.get('http://www.hnep.gov.cn:98/')
com_list = driver.find_element_by_xpath('//*[@id="UpdatePanel2"]/div[3]/table/tbody')
print(com_list.text)

print('===============================================')

driver.find_element_by_xpath('//*[@id="asp_enpnomon"]/table/tbody/tr/td[1]/a[3]').click()
sleep(20)
com_list2 = driver.find_element_by_xpath('//*[@id="UpdatePanel2"]/div[3]/table/tbody')
print(com_list2.text)
print('================================================')

sleep(3)
driver.find_element_by_xpath('//*[@id="asp_enpnomon"]/table/tbody/tr/td[1]/a[3]').click()
sleep(20)
com_list2 = driver.find_element_by_xpath('//*[@id="UpdatePanel2"]/div[3]/table/tbody')
print(com_list2.text)
print('================================================')

sleep(3)
driver.quit()