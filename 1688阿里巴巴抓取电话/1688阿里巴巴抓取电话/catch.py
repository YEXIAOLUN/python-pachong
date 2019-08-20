# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 20:06:18 2019

@author: YEXIAOLUN
"""
import xlwt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#url='https://s.1688.com/company/company_search.htm?keywords=%BA%CF%B7%CA&n=y&netType=1%2C11&spm='

def main():
    book = xlwt.Workbook()
    sheet = book.add_sheet('Sheet1')
    index=1
    sheet.write(0,0,'公司名称')
    sheet.write(0,1,'联系人')
    sheet.write(0,2,'职位')
    sheet.write(0,3,'电话')
    sheet.write(0,4,'移动电话')
    sheet.write(0,5,'地址')
    logindriver=webdriver.Chrome()
    logindriver.maximize_window()
    logindriver.get('https://login.1688.com/member/signin.htm?spm=a2615.2177701.autotrace-smt_topbar.d3.6d8156d4b1OqdC&Done=https%3A%2F%2Fshop1458752305488.1688.com%2F')
    input('请登录')
    page=1
    cookies=logindriver.get_cookies()
    logindriver.quit()
    chrome_options = Options()
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    #chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    #url='https://s.1688.com/company/company_search.htm?keywords=%BA%CF%B7%CA&n=y&netType='+spam+'&sortType=pop&pageSize=30&offset=3&beginPage='+str(page)
    url='https://s.1688.com/company/company_search.htm?keywords=%B0%B2%BB%D5&button_click=top&earseDirect=false&n=y&netType=1%2C11&sortType=pop&pageSize=30&offset=3&beginPage=1'
    driver.get(url)
    for co in cookies:
        try:
            driver.add_cookie(co)
        except:
            pass
    
    while 1:
        url='https://s.1688.com/company/company_search.htm?keywords=%B0%B2%BB%D5&button_click=top&earseDirect=false&n=y&netType=1%2C11&sortType=pop&pageSize=30&offset=3&beginPage='+str(page)
        driver.get(url)
        if '小二正忙' in driver.page_source:
            input('滑动验证码')
        try:
            driver.find_element_by_class_name('noresult-hd').text
            break
        except:
            pass
        items=driver.find_elements_by_class_name('company-list-item')
        itemurl=[]
        companytext=[]
        for item in items:
            company=item.find_element_by_class_name('list-item-title-text').text
            u=item.find_element_by_class_name('list-item-title-text').get_attribute('href')
            itemurl.append(u)
            companytext.append(company)
        for u,com in zip(itemurl,companytext):
            try:
                driver.get(u)
            except:
                pass
            try:
                ul=driver.find_element_by_partial_link_text('联系方式').get_attribute('href')
            except:
                try:
                    ul=driver.find_element_by_partial_link_text('公司档案').get_attribute('href')
                except:
                    continue
            driver.get(ul)
            dts=driver.find_elements_by_css_selector('dl')
            mobie=''
            person=''
            info=''
            for d in dts:
                if '联系人' in d.text.replace(' ',''):
                    try:
                        person=d.text.split('\n')[1].split('（')[0].split(' ')[0]
                        info=d.text.split('\n')[1].split('（')[1].replace('）','')
                    except:
                        pass
                if '电话' in d.text.replace(' ',''):
                    mobie=d.text.split('\n')[-1]
                    break
            try:
                addr=driver.find_element_by_class_name('address').text
            except:
                addr=''
            try:
                phone=driver.find_element_by_class_name('m-mobilephone').text.split('\n')[-1]
            except:
                phone=''
            print(com,phone)
            sheet.write(index,0,com)
            sheet.write(index,1,person)
            sheet.write(index,2,info)
            sheet.write(index,3,mobie)
            sheet.write(index,4,phone)
            sheet.write(index,5,addr)
            index+=1
            book.save('1688公司联系方式.xls')
        page+=1
if __name__ == '__main__':
    #pass
    main()