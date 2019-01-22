# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:03:25 2018

@author: Administrator
"""

from selenium import webdriver
import requests
def main(word,size):
    url='https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word='+word+'&step_word=&hs=0&pn=0&spn=0&di=124284271760&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=2458882593%2C105553851&os=2801383267%2C3364038249&simid=0%2C0&adpicid=0&lpn=0&ln=1894&fr=&fmq=1543553313940_R&fm=index&ic=0&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=girl&bdtype=0&oriquery=&objurl=http%3A%2F%2Fn4-q.mafengwo.net%2Fs9%2FM00%2F75%2F2E%2FwKgBs1hh8s6AHfphABit5OakEEU21.jpeg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B4wujg2o5_z%26e3BvgAzdH3Fojg2AzdH3F1jpwts_z%26e3Brir%3Ft1%3D8cc9b9nnnlccmacl&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&selected_tags=0'
    driver=webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(30)
    lists=[]
    for i in range(0,size):
        driver.find_element_by_class_name('img-next').click()
        src=driver.find_element_by_class_name('currentImg').get_attribute('src')
        lists.append(src)
    for i,j in enumerate(lists):
        try:
            res=requests.get(j,timeout=1)
        except:
            driver.implicitly_wait(0)
        with open('d://pictures//'+str(i)+'.jpg','wb') as f:
            f.write(res.content)
    driver.quit()
if __name__ =='main':
    main()
