# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 22:23:08 2018

@author: Administrator
"""

import requests
import bs4
import pymysql
def save(news,newslink,types):
    db=pymysql.connect('localhost','root','123456','news',charset='utf8')
    cursor=db.cursor()
    for i in range(0,len(news)):
        print(i)
        sql='insert into newinfo values(%s,%s,%s,%s,%s);'
        cursor.execute(sql, [types+str(i),news[i],newslink[i],types,0])
        db.commit()
    cursor.close()
    db.close()
def get():
    url='https://news.qq.com'
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
    res=requests.get(url,headers=headers)
    bs=bs4.BeautifulSoup(res.text,'lxml')
    bs2=bs.findAll(class_='cf')
    news=[]
    newslink=[]
    for i in bs2:
        print(i)
        try:
            a=i.find(class_='detail').find('a')
            print(i)
            news.append(a.text.split('\t')[0].strip())
            newslink.append(a.find('a').get_attribute_list('href')[0])
        except:
            pass
    return news,newslink

def t():
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
    types=['world','milite','history','cul','visit']
    for i,z in enumerate(types):
        print(z)
        url='https://new.qq.com/ch/'+z
        res=requests.get(url,headers=headers)
        bs=bs4.BeautifulSoup(res.text,'lxml')
        bs2=bs.findAll(class_='cf')
        news=[]
        newslink=[]
        for j in bs2:
            try:
                a=j.find(class_='detail').find('a')
                news.append(a.text)
                newslink.append(a.get_attribute_list('href')[0])
            except:
                pass
        save(news,newslink,z)
if __name__ == "__main__":
    #news,newslink=get()
    #save(news,newslink,'news')
    #t()

