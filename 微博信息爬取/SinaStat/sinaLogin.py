# -*- coding: utf-8 -*-

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import requests
import os
from time import sleep
def account(driver):
    account=str(input('请输入账号'))
    password=str(input('请输入密码'))
    driver.find_elements_by_class_name('W_input')[1].clear()
    driver.find_elements_by_class_name('W_input')[1].send_keys(account)
    driver.find_elements_by_class_name('W_input')[2].clear()
    driver.find_elements_by_class_name('W_input')[2].send_keys(password)
    driver.find_element_by_class_name('W_btn_a').click()
    driver.implicitly_wait(10)
def login(driver):
    url=driver.current_url
    while(driver.current_url==url):
        try:
            account(driver)
            if(driver.current!=url):break
            img=driver.find_element_by_xpath('//img[@node-type="verifycode_image"]').get_attribute('src')
            res=requests.get(img)
            f=open(os.getcwd()+'code.png','wb')
            f.write(res.content)
            f.flush()
            f.close()
            lena = mpimg.imread(os.getcwd()+'code.png')
            lena.shape
            plt.imshow(lena)
            plt.axis('off')
            plt.show()
            code=str(input('输入验证码'))
            driver.find_elements_by_class_name('W_input')[3].clear()
            driver.find_elements_by_class_name('W_input')[3].send_keys(code)
            driver.find_element_by_class_name('W_btn_a').click()
            driver.implicitly_wait(10)
            print(driver.current_url,url)
            if(driver.current_url==url):print('账号密码或者验证码错误，请重新输入')
        except:
            driver.implicitly_wait(0)
    driver.implicitly_wait(10)
    el=driver.find_elements_by_class_name('S_txt1')
    el[4].click()
    driver.implicitly_wait(10)
    #find(i)
def find(driver,word):
    error=1
    worditem=[]
    try:
        el=driver.find_elements_by_class_name('S_txt1')
        el[4].click()
        driver.implicitly_wait(10)
        driver.find_element_by_link_text(word).click()
        item=0
        lens=0
        while(item<9):  
            el=driver.find_elements_by_class_name('WB_cardwrap')
            sleep(5)
            for i,j in enumerate(el):
                if(i>=lens and i<len(el)-2):
                    move(driver,j)
                    sleep(1)
                    ell=j.find_elements_by_class_name('line')
                    try:
                        num=int(ell[1].text.split()[-1])
                        if(num>500):
                            item+=1
                            try:
                                a=j.find_element_by_partial_link_text('月')
                            except:
                                a=j.find_element_by_partial_link_text('今天')
                            worditem.append(a.get_attribute('href'))
                            with open('d://a.txt','a') as f:
                                f.write(a.get_attribute('href')+'\n')
                    except:
                        driver.implicitly_wait(0)
            lens=len(el)
            down(driver)
            if(item>10):break
        print('url获取成功')
        return worditem
    except :
        print('网络错误，正在重新获取，请稍等')
        error+=1
        if(error<5):
             find(driver,word)
        else:
            print('获取失败')
def down(driver):
    foldpagewg = driver.find_element_by_class_name('company')
    driver.execute_script('arguments[0].scrollIntoView();', foldpagewg)
def move(driver,foldpage):
    driver.execute_script('arguments[0].scrollIntoView();', foldpage)
