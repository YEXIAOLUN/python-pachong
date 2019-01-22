# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 21:42:01 2018

@author: Administrator
"""

from selenium import webdriver
import csv
def write(driver):
    size=int(input('输入爬取总量'))
    s=input('输入文件名')
    f=open('C:\\Users\\Administrator\\Desktop\\'+s,'a',newline='')
    wr=csv.writer(f,dialect='excel')
    lists=['商品名称','商品id','商品价格','商品库存','商品销量','发布时间','商家编码']
    wr.writerow(lists)
    count=0
    while(count<size):
        sums=driver.find_elements_by_class_name('with-sid')
        goods=driver.find_elements_by_class_name('goods-sid')
        for j,i in enumerate(sums):
            li=[]
            name=''
            id_=''
            price=''
            ku=''
            xiao=''
            time=''
            bian=''
            try:
                strs=i.text.split('\n')
                name=strs[0]
                id_=strs[1]
                price=strs[2]
                ku=strs[3]
                strs1=strs[4].split(' ')
                xiao=strs1[0]
                strs2=strs[5].split(' ')
                time=strs1[1]+'-'+strs2[0]
                bian=goods[j].text
            except:
                pass
            li.append(name)
            li.append(id_)
            li.append(price)
            li.append(ku)
            li.append(xiao)
            li.append(time)
            li.append(bian)
            #print(li)
            wr.writerow(li)
            count+=1
            if(count>size):
                break
        if(count>size):
            break
        driver.find_element_by_class_name('next-page').click()
        driver.implicitly_wait(20)
    f.flush()
    f.close()
   
if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get('https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d94WJVsg&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F')
    while(True):
        if('sell' in driver.current_url):
            url='https://sell.taobao.com/auction/merchandise/auction_list.htm?spm=a1z09.1.favorite.d45.33863606GImSGH'
            driver.get(url)
            write(driver)
            break