# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:57:36 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:02:33 2018

@author: Administrator
"""

from  selenium import webdriver
from time import sleep
import pandas as pd
def main():
    driver=webdriver.Chrome()
    driver.maximize_window()
    url=str(input('输入url'))
    sums=int(input('输入要爬取的评论总数'))
    driver.get(url)
    driver.implicitly_wait(10)
    if 'tmall' in url:
        allInfo = findtm(driver,sums)
    else:
        allInfo=findtb(driver,sums)
        
    data = pd.DataFrame(columns=['用户名', '颜色分类','评论','时间'])
    for item in allInfo:
        data.loc[len(data)] = [item[0], item[1], item[2], item[3]]
    
    data.to_excel("商品评论2.xlsx")   
    driver.quit()     

def findtm(driver,sums):
    count=[]
    driver.find_element_by_class_name('sufei-dialog-close').click()  #关闭登录
    price=driver.find_element_by_class_name('tm-price').text  #获取商品价格
    tm_count=driver.find_element_by_class_name('tm-count').text  #获取商品评论总数
    info=driver.find_element_by_id('J_AttrUL').text.split('\n')  #获取商品信息 
    print(price)
    print(tm_count)
    print(info)
    driver.execute_script("window.scrollBy(0,800)")
    sleep(5)
    driver.find_element_by_class_name('J_ReviewsCount').click()
    while(len(count)<sums):
        comment=driver.find_elements_by_class_name('tm-rate-fulltxt')  #用户评论
        time=driver.find_elements_by_class_name('tm-rate-date')   #发布时间
        types=driver.find_elements_by_class_name('rate-sku')  #采购类型
        names=driver.find_elements_by_class_name('rate-user-info')  #用户id
        for i in range(20):
            person=[]
            person.append(names[i].text)
            person.append(types[i].text)
            person.append(comment[i].text)
            person.append(time[i].text)
            print(person)
            count.append(person)
        try:
            driver.find_element_by_link_text('下一页>>').click()
        except:
            print('没有下一页了喔')
            break
        sleep(2)
#        print(count)
    return count


def findtb(driver,sums):
    count=[]
    driver.find_element_by_class_name('sufei-dialog-close').click()  #关闭登录
    driver.find_element_by_class_name('J_ReviewsCount').click()
    sleep(2)
    driver.implicitly_wait(10)
    while(len(count)<sums):
        comment=driver.find_elements_by_class_name('J_KgRate_ReviewContent')  #用户评论
        time=driver.find_elements_by_class_name('tb-r-date')   #发布时间
        types=driver.find_elements_by_class_name('tb-r-info')  #采购类型
        names=driver.find_elements_by_class_name('from-whom')  #用户id
        for i in range(20):
            person=[]
            person.append(names[i].text)
            person.append(types[0].text.split(time[0].text)[1])
            person.append(comment[i].text)
            person.append(time[i].text)
            
            print(person)
            count.append(person)
        driver.find_element_by_class_name('pg-next').click()
        try:
            driver.find_element_by_class_name('pg-disabled')
            print('没有下一页了喔')
            break
        except:
            sleep(0)
        sleep(2)
#        print(count)
    return count


if __name__ == "__main__":
    main()


