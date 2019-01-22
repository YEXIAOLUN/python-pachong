# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:26:19 2018

@author: Administrator
"""
from selenium import webdriver
from time import sleep
from sinaLogin import *
from sendInfo import *
from sendLevel import *
import pandas as pd

def main():
    word1=['数码','养生','正能量','房产','读书']
    word2=['综艺','明星','星座','美妆','时尚']
    word3=['社会','国际','军事','法律','政务']
    driver=webdriver.Chrome()
    driver.get('https://weibo.com/')
    driver.maximize_window()
    sleep(5)
   # x = input("请输入:")
    data = pd.DataFrame(columns=['类别','文章地址','用户名','主页链接','性别','年龄','是否大V','来自城市','微博等级','转发内容','转发数','评论数','点赞数','转发级联','转发时间'])    
    login(driver)
    print(word1, word2, word3)
    #word = '明星'
    word = input("输入查找的类别")
    worditem=find(driver,word)#返回所有满足条件数量推文的URL
    print(worditem) 
    allPage=[]
    for i in worditem:
        talkurl=talk(driver,i)#返回所有满足条件的用户URL
        ans = comment(driver,talkurl[1])
        data.loc[len(data)] = [word, talkurl[1], ans[0], ans[1], ans[4], ans[5], ans[6], ans[7], ans[8], ans[9], ans[10], ans[11], ans[12], 0, talkurl[2]]
        for j in talkurl[0].keys():
            ans = comment(driver,j)#返回满足条件的转发用户信息
            data.loc[len(data)] = [word, talkurl[1], ans[2], ans[3], ans[4], ans[5], ans[6], ans[7], ans[8], ans[9], ans[10], ans[11], ans[12], talkurl[0][j][0], talkurl[0][j][1]]
            data.to_excel(word+".xlsx")
        #print(data)
if __name__ == '__main__':
    main()        
