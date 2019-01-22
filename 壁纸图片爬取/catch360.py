# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:58:10 2018

@author: Administrator
"""
from selenium import webdriver
import requests
def main(word,size):
    url='http://image.so.com/v?q='+word+'&src=srp&cmsid=57588782140b3fd458fd1c857091abc3&cmran=0&cmras=6&cn=0&gn=0&kn=6#id=2631093bb4cca4234845fcabc53baba9&itemindex=0&currsn=0&jdx=12&gsrc=1&fsn=66&multiple=0&dataindex=12&prevsn=0'
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(30)
    try:
        driver.find_element_by_class_name('cm-tip-mode').click()
    except:
        driver.implicitly_wait(0)
    lists=[]
    for i in range(0,size):
        src=driver.find_element_by_class_name('lb_mainimg').get_attribute('src')
        lists.append(src)
        driver.find_element_by_class_name('lb_next').click()
    for i,j in enumerate(lists):
        try:
            res=requests.get(j,timeout=1)
        except:
            driver.implicitly_wait(0)
        with open('d://pictures//'+str(i)+'.jpg','wb') as f:
            f.write(res.content)
if __name__ =='main':
    main()
    
