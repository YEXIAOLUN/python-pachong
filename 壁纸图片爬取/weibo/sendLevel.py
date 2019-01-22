# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 10:39:54 2018

@author: Administrator
"""
'''
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
'''
from time import sleep
def talk(driver,url):
    talkurl=[]
    driver.get(url+'?type=repost')
    driver.implicitly_wait(10)
    talkcount=1
    try:
        author=driver.find_element_by_xpath("//span[contains(text(),'同时评论给原文作者')]") #检查该微博是否为源微博
        href=driver.find_element_by_class_name('line')
        href=href.find_element_by_class_name('S_txt2').get_attribute('href')
        driver.get(href)
        driver.implicitly_wait(10)
    except:
        href=url
        driver.implicitly_wait(0
                               
                               
                               )
    try:
        driver.find_element_by_class_name('between_line')
        flag=False
    except:
        flag=True
    while(talkcount<201):  #循环同级出200条评论
        list_url=driver.find_element_by_class_name('list_ul')
        li=list_url.find_elements_by_css_selector('div') #取出热门微博
        for i in li:
            if flag==True and 'list_li' in i.get_attribute('class'):
                a=i.find_element_by_class_name('WB_text')
                userName=a.find_element_by_css_selector('a').text  #用户名
                a=a.find_element_by_css_selector('a').get_attribute('href')  #用户主页链接
                texta=i.find_element_by_class_name('WB_from').find_element_by_css_selector('a')
                textatime=texta.text #获取转发时间
                texta=texta.get_attribute('href') #用户转发微博链接
                
                els=i.find_element_by_css_selector('span')
                lens=0  #转发分级
                for j in els.text:
                    if '@' in j:lens+=1
                talkurl.append(texta)
                print(userName+':'+a+' 转发'+str(lens+1)+'级转发'+'转发时间:'+textatime)
                talkcount+=1
            if 'between_line' in i.get_attribute('class'):
                flag=True
        driver.find_element_by_class_name('next').click()
        sleep(5)
    return talkurl,str(lens+1),href
    
    
    
                