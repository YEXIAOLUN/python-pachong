# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 19:32:04 2019

@author: Administrator
"""

import xlrd
from selenium import webdriver
def getcompany():  #获得所有公司名称
    workbook=xlrd.open_workbook(r'd://equity5.xls')
    sheet1=workbook.sheet_by_name('Sheet1')
    company=sheet1.col_values(1)
    company=company[1:12799]
    return company
def getcompanyType(driver,url,companyTypeName):   #判断该公司是否显示性质或能否找到该公司
    #if(len(companyTypeName)>index):
        #return companyTypeName,True
    driver.get(url)
    t=''
    try:
        t=driver.find_element_by_class_name('-border-top-none').text
    except:
        pass
    text=driver.find_elements_by_class_name('block-data')
    texts=text[0].text+text[1].text+t
    texts=texts.split('\n')   #所有包含信息公司的文本
    for i in texts:   #抓取规则
        if '公司类型' in i:
            print(i)
            if '国有' in i:
                print('国有')
                companyTypeName.append('国有')
                bo=True
                index+=1
                break
            elif ('自然人' in i and not '非自然人' in i) or '内资' in i or '个体' in i or '个人' in i:
                print('个人')
                companyTypeName.append('个人')
                bo=True
                index+=1
                break
            elif '外国' in i or '台港澳' in i or '外商投资' in i or '外商投资' in i:
                print('外资')
                companyTypeName.append('外资')
                bo=True
                index+=1
                break
            elif '中外合作' in i or '中外合资' in i  :
                print('中外合作')
                companyTypeName.append('中外合作')
                bo=True
                index+=1
                break
            elif '集体所有制' in i or '全民所有制' in i or '股份合作' in i or '集体企业' in i:
                print('集体所有制')
                companyTypeName.append('集体所有制')
                bo=True
                index+=1
                break
            else:
                d1=driver.find_element_by_class_name('dagudong')
                if( not '公司' in d1.text and not '股东' in d1.find_element_by_css_selector('a').text and 
                    not '资委' in d1.find_element_by_css_selector('a').text and 
                    not '委员会' in d1.find_element_by_css_selector('a').text and 
                    not '财政厅' in d1.find_element_by_css_selector('a').text):
                    print('个人2')
                    companyTypeName.append('个人')
                    bo=True
                    index+=1
                    break
                else:
                    d2=d1.find_element_by_css_selector('a')
                    companyTypaName,bo=getcompanyType(driver,d2.get_attribute('href'),companyTypeName)  #判断该公司下一级股东性质
        elif '公司类别' in i:
            print(i)
            if '私人' in i:
                print('个人')
                companyTypeName.append('个人')
                bo=True
                index+=1
                break
        elif '最终控制人' in i:
            print(i)
            bo=True
            if '国有' in i:
                print('国有')
                companyTypeName.append('国有')
                bo=True
                index+=1
                break
            elif '持有' in i:
                print('个人3')
                companyTypeName.append('个人')
                bo=True
                index+=1
                break
        elif '登记机关' in i:
            if '台北市' in i:
                print('外资')
                companyTypeName.append('外资')
                bo=True
                index+=1
                break
    if not bo:  #判断该公司是否有公司性质
        print('该公司已经注销或者其他原因')
        companyTypeName.append('Null')
        bo=True
        index+=1
    return companyTypeName,bo
def save(companyTypeName):    #抓取的结果保存在新建的excel文件里
    import xlwt
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    for i,j in enumerate(companyTypeName):
        sheet.write(i,0,j)#第0行第一列写入内容
    wbk.save('d://company1.xls')
def main(companylist):
    driver=webdriver.Chrome()    #selenium模拟访问浏览器爬取渲染过的页面
    driver.maximize_window()
    url='https://www.tianyancha.com/search?key='
    companyTypeName=[]  #所有公司性质
    index=0
    for i in companylist:
        try:
            driver.find_element_by_class_name('wapHeader')
        except:
            pass
        print(i)
        driver.get(url+i)
        index+=1
        try:
            driver.find_element_by_class_name('result-tips')
            result1=driver.find_element_by_class_name('search-item')
            a=result1.find_element_by_css_selector('a')
            companyurl=a.get_attribute('href')
            bo=False
            try:
                companyTypeName,bo=getcompanyType(driver,companyurl,companyTypeName)  
            except:
                pass
            if (not bo) and (len(companyTypeName)<index):   #判断是否获取到公司性质
                companyTypeName.append('Null')
            companyTypeName=companyTypeName[0:index]   #爬取一个连接的终止条件
        except:   #判断该公司是否能找到
            print('未搜索到该公司')
            companyTypeName.append('Null')
            pass
    save(companyTypeName)  





if __name__ == "__main__":
    company=getcompany()   #所有公司名称
    pass
