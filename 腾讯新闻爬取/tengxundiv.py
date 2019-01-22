# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:51:59 2018

@author: Administrator
"""

import pymysql
import bs4
import requests
import os
def sql(path):
    db=pymysql.connect('localhost','root','123456','new',charset='utf8')
    cursor=db.cursor()
    sql='select newsid,url from newsinfo'
    cursor.execute(sql)
    url=cursor.fetchall()
    count=0
    for i in url:
        count+=1
        d=div(i[1])
        with open(path+'\\'+i[0]+'.jsp','w',encoding='utf8') as f:
            f.write(str(d))
def div(texturl):
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
    res=requests.get(texturl,headers=headers)
    bs=bs4.BeautifulSoup(res.text,'lxml')
    div=bs.find(class_='LEFT')
    return div

if __name__ == "__main__":
    path='C:\\Users\\Administrator\\Desktop\\news'
    if not os.path.exists(path):
        os.mkdir(path)
    sql(path)