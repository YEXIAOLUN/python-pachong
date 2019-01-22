# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:58:48 2018

@author: Administrator
"""

import requests
import bs4
import os
words={'风景':'fengjing','动漫':'dongman','美女':'meinv','创意':'chuangyi','卡通':'katong',
      '汽车':'qiche','游戏':'youxi','可爱':'keai','明星':'mingxing','建筑':'jianzhu'}
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
def main(word,size):
    url='http://desk.zol.com.cn/'
    url1=url+words.get(word)+'/'
    res=requests.get(url1,headers=headers)          #搜寻所有图片建立请求
    res.encoding='gbk'                              #设置网页字符格式
    bs=bs4.BeautifulSoup(res.text,'lxml')                 
    b=bs.findAll(class_='photo-list-padding')       #所有符合要求图集
    count=0
    while(count<size):
        for i in b:
            pic=i.find(class_='pic')
            src=url+pic.get_attribute_list('href')[0]                #每个图集链接
            res2=requests.get(src,headers=headers)
            bs2=bs4.BeautifulSoup(res2.text,'lxml')
            img=bs2.find(id='showImg')
            li=img.findAll('li')  
            file='d://pictures//'+pic.find('span').get_attribute_list('title')[0]
            os.makedirs(file)                   
            for j in li:
                href=url+j.find('a').get_attribute_list('href')[0]             #图集中每个图片链接
                res3=requests.get(href,headers=headers)
                bs3=bs4.BeautifulSoup(res3.text,'lxml')
                try:
                    xs=bs3.find(id='1920x1080')
                    xshref=url+xs.get_attribute_list('href')[0]
                    res4=requests.get(xshref,headers=headers)
                    bs5=bs4.BeautifulSoup(res4.text,'lxml')
                    imghref=bs5.find('img').get_attribute_list('src')[0]
                    end=requests.get(imghref)
                    with open(file+'//'+str(count)+'.jpg','wb') as f:
                        f.write(end.content)
                    count+=1
                    if(count>=size):
                        break
                except:
                    continue
            if(count>=size):
                    break
if __name__ =='main':
    main()
