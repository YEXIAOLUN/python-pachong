# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:32:20 2018

@author: Administrator
"""
import os
import requests
import pytesseract
from PIL import Image
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
url=str(input('请输入你的网址'))
options=webdriver.ChromeOptions()
options.set_headless()
options.add_argument('--disable-gpu')
driver=webdriver.Chrome(options=options)
driver.maximize_window()
try:
    driver.get(url)
    driver.implicitly_wait(30)   
except:
    print('网址不正确或者连接超时等其他原因')
types=str(driver.find_element_by_class_name('reader-container').get_attribute('class'))
if 'xreader' in types:
    p1=driver.find_element_by_class_name('reader-page-1').text
elif 'txt' in types:
    p1=driver.find_element_by_id('reader-pageNo-1').text
else:
    p1url=driver.find_element_by_class_name('reader-pageNo-1').find_element_by_css_selector('img').get_attribute('src')
    p1=requests.get(p1url).content
    f1=open('d://a.jpg','wb')
    f1.write(p1)
    f1.flush()
    image=Image.open('d://a.jpg')
    p1=pytesseract.image_to_string(image,lang='chi_sim')
try:
    foldpagewg = driver.find_element_by_class_name('banner-core-wrap')
    driver.execute_script('arguments[0].scrollIntoView();', foldpagewg)
    driver.find_element_by_class_name('fc2e').click()
    driver.implicitly_wait(30)
except:
    print('没有剩余页')
count=int(driver.find_element_by_class_name('page-count').text[1:])
with open('d://a.txt','wb') as f:
    f.write(p1.encode('utf8'))
    for i in range(1,count+1):
        driver.find_element_by_xpath("//input[@class='page-input']").clear()
        driver.find_element_by_xpath("//input[@class='page-input']").send_keys(i)
        driver.find_element_by_xpath("//input[@class='page-input']").send_keys(Keys.ENTER)
        sleep(1)
        if 'xreader' in types:
            page='reader-page-'+str(i)
            p1=driver.find_element_by_class_name(page).text
            f.write(p1.encode('utf8'))
        elif 'txt' in types:
            page='reader-pageNo-'+str(i)
            p1=driver.find_element_by_id(page).text
            f.write(p1.encode('utf8'))
        else:
            page='reader-pageNo-'+str(i)
            p1url=driver.find_element_by_class_name(page).find_element_by_css_selector('img').get_attribute('src')
            p1=requests.get(p1url).content
            f1=open('d://a.jpg','wb')
            f1.write(p1)
            f1.flush()
            image=Image.open('d://a.jpg')
            p1=pytesseract.image_to_string(image,lang='chi_sim')
            f.write(p1.encode('utf8'))
print('文件保存成功，目标文件是d://a.txt')
driver.quit()
os.system('pause')