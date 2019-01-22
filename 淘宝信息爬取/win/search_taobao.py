# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 23:07:19 2018

@author: Administrator
"""

from selenium import webdriver
import requests
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from time import sleep
import pandas as pd
def login(driver):
    driver.get('https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d94WJVsg&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F')
    img_src=driver.find_element_by_class_name('qrcode-img').find_element_by_css_selector('img').get_attribute('src')
    res=requests.get(img_src)
    with open(os.getcwd()+'.png','wb') as f:
        f.write(res.content)
    print('请使用二维码登录')
    imgs=mpimg.imread(os.getcwd()+'.png')
    imgs.shape
    plt.imshow(imgs)
    plt.axis('off')
    plt.show()
    sleep(1)    
def find(driver):
    ci=str(input('输入要查找的关键词'))
    sums=int(input('输入要获取多少商品'))
    count=0
    driver.find_element_by_class_name('search-combobox-input').clear()
    driver.find_element_by_class_name('search-combobox-input').send_keys(ci)
    driver.find_element_by_class_name('btn-search').click()
    items=driver.find_elements_by_class_name('J_MouserOnverReq')
    lists=[]
    while(count<sums):
        for i in items:
            good=[]
            link=i.find_element_by_class_name('pic-link').get_attribute('href')
            price=i.find_element_by_class_name('price').text
            persons=i.find_element_by_class_name('deal-cnt').text
            name=i.find_element_by_class_name('row-2').text
            shop=i.find_element_by_class_name('shop').text
            location=i.find_element_by_class_name('location').text
            good.append(link)
            good.append(price)
            good.append(persons)
            good.append(name)
            good.append(shop)
            good.append(location)
            lists.append(good)
            print(good)
            count+=1
            if(count==sums):break
        if(count==sums):break
        driver.find_element_by_xpath('//a[@title="下一页"]').click()
        sleep(1)
        items=driver.find_elements_by_class_name('J_MouserOnverReq')
    return lists
def main():
  driver=webdriver.Chrome()
  driver.maximize_window()  
  login(driver)
  sleep(1)
  driver.refresh()
  allInfo=find(driver)
  data = pd.DataFrame(columns=['链接', '价格','购买人数','商品名称','店家名称','位置'])
  for item in allInfo:
          data.loc[len(data)] = [item[0], item[1], item[2], item[3],item[4],item[5]]
  data.to_excel("商品信息.xlsx")  
  driver.quit() 
if __name__ == "__main__":
    main()
  