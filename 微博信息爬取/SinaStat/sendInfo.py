# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:49:07 2018

@author: Administrator

"""
'''
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
'''

def comment(driver,url):
    driver.get(url+'?type=repost')
    driver.implicitly_wait(10)
    try:
        com=driver.find_elements_by_class_name('pos')
        sendCnt=com[1].find_element_by_class_name('W_ficon').text
        sendCnt=com[1].text.split(sendCnt)[1]
        if('转发' in sendCnt):sendCnt=0
        talkCnt=com[2].find_element_by_class_name('W_ficon').text
        talkCnt=com[2].text.split(talkCnt)[1]
        if('评论' in talkCnt):talkCnt=0
        goodCnt=com[3].find_element_by_class_name('W_ficon').text
        goodCnt=com[3].text.split(goodCnt)[1]
        if('赞' in goodCnt):goodCnt=0
    except:
        sendCnt=0
        talkCnt=0
        goodCnt=0
    content=driver.find_element_by_class_name('WB_text').text
    try:
        author=driver.find_element_by_xpath("//span[contains(text(),'同时评论给原文作者')]").text.split()[-1]
        author='@'+author
        author=driver.find_element_by_link_text(author).text
    except:
        author=driver.find_element_by_class_name('WB_info').text
    userName=driver.find_element_by_class_name('WB_info')   
    authorlink=userName.find_element_by_class_name('W_fb').get_attribute('href')
    userName=userName.text
    driver.get(authorlink)
    driver.implicitly_wait(10)
    try:
        grade=driver.find_element_by_class_name('W_icon_level')
        grade=grade.text
    except:
        grade='null'
    isBigv=False
    try:
        isBigv=driver.find_element_by_class_name('icon_verify_co_v')
        isBigv=True
    except:
        driver.implicitly_wait(0)
    try:
        isBigv=driver.find_element_by_class_name('icon_verify_v')
        isBigv=True
    except:
        driver.implicitly_wait(0)  
    try:
        sex=driver.find_element_by_class_name('icon_pf_male')
        sex='男'
    except:
        sex='女'
    perdata=driver.find_element_by_xpath('//ul[@class="ul_detail"]')
    perdatas=perdata.find_elements_by_css_selector('li')
    place='null'
    age=0
    for i in perdatas:
        try:
            if i.find_element_by_class_name('ficon_cd_place'):
                place=i.text.split('\n')[1].split()[0]
        except:
            driver.implicitly_wait(0)
        try:
            if i.find_element_by_class_name('ficon_constellation'):
                age=2018-int(i.text.split('\n')[1].split('年')[0])
        except:
            driver.implicitly_wait(0)
    person=[]
    person.append(author)
    person.append(url)
    person.append(userName)
    person.append(authorlink)
    person.append(sex)
    person.append(age)
    person.append(isBigv)
    person.append(place)
    person.append(grade)
    person.append(content)
    person.append(sendCnt)
    person.append(talkCnt)
    person.append(goodCnt)
    
    print('文章作者:',author)
    print('文章链接:',url)
    print('用户名:',userName)
    print('主页链接:',authorlink)
    print('性别：',sex)
    print('转发用户年龄：',age)
    print('是否大V：',isBigv)
    print('来自的省份:',place)
    print('用户等级：',grade)
    #print('转发内容：',content)
    print('转发数:',sendCnt)
    print('评论数：',talkCnt)
    print('点赞数：',goodCnt)
    
    return person
    
    
