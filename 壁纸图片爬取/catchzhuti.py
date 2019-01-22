# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 21:38:40 2018

@author: Administrator
"""
import requests
import bs4
import os
words={'美食':'meishi','小清新':'xiaoqingxin','植物':'zhiwu','游戏':'youxi','帅哥':'shuaige',
       '汽车':'qiche','美女':'meinv','军事':'junshi','家居':'jiaju','风景':'fengjing'}
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
def main(word,size):
    url='http://www.win4000.com/zt/'+words.get(word)+'.html'
    res=requests.get(url,headers=headers)
    bs=bs4.BeautifulSoup(res.text,'lxml')
    bs2=bs.findAll(class_='clearfix')[5]
    li=bs2.findAll('li')  #所有图集链接
    count=0
    while(count<size):
        for i in li:
            src=i.find('a').get_attribute_list('href')[0]
            res2=requests.get(src,headers=headers)
            bbs=bs4.BeautifulSoup(res2.text,'lxml')             
            bbs2=bbs.find(class_='scroll-img')
            li2=bbs2.findAll('li')        #图集所有图片链接
            file='d://pictures//'+i.find('p').text
            os.makedirs(file)               
            for j in li2:
                a=j.find('a')
                href=a.get_attribute_list('href')[0]
                pic=requests.get(href,headers=headers)
                bbbs=bs4.BeautifulSoup(pic.text,'lxml')
                bbbs2=bbbs.find(class_='pic-large').get_attribute_list('src')[0]
                with open(file+'//'+str(count)+'.jpg','wb') as f:
                    xs=requests.get(bbbs2)
                    f.write(xs.content)
                count+=1
                if(count>=size):
                    break
            if(count>=size):
                    break
if __name__ =='main':
    main()
