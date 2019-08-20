from selenium import webdriver
import xlwt
from time import sleep
import win32api,win32con
global comli
comli=[]

def main():
    global comli
    book = xlwt.Workbook()
    sheet = book.add_sheet('Sheet1')
    sheet.write(0,0,'公司名称')
    driver=webdriver.Chrome()
    driver.maximize_window()
    url='https://sou.zhaopin.com/?jl=765&re=2042&sf=0&st=0&kw=%E5%A4%96%E8%B4%B8%E4%B8%9A%E5%8A%A1%E5%91%98&kt=3'
    driver.get(url)
    input('确认好相应的信息，然后按1爬取：')
    index =1
    while 1:
        js_top = "var q=document.documentElement.scrollTop=0"
        driver.execute_script(js_top)  
        sleep(2)
        coms=driver.find_elements_by_class_name('company_title')
        for c in coms:
            try:
                sheet.write(index,0,c.text)
                book.save('1.xls')
                index+=1
                comli.append(c.text)
            except:
                pass
        js="var q=document.documentElement.scrollTop=100000"  
        driver.execute_script(js)  
        sleep(2)
        cuurl=driver.current_url
        slindex=0
        while 1:
            try:
                driver.find_elements_by_class_name('soupager__btn')[1].click()
                if cuurl!=driver.current_url:break
            except:
                sleep(1)
            slindex+=1
            if slindex>=5:break
        if cuurl == driver.current_url:break
    sleep(120)
    main2(driver,book,sheet,index)
def main2(driver,book,sheet,index):
    global comli
    js="var q=document.documentElement.scrollTop=100000"  
    js_top = "var q=document.documentElement.scrollTop=0"
    while 1:
        driver.execute_script(js)  
        sleep(2)
        while 1:
            try:
                driver.find_element_by_xpath('//input[@class="soupager__pagebox__goinp"]').clear()
                driver.find_element_by_xpath('//input[@class="soupager__pagebox__goinp"]').send_keys('1')
                driver.find_elements_by_class_name('soupager__btn')[2].click()
                break
            except:
                pass
        notli=[]
        while 1:
            driver.execute_script(js_top)  
            sleep(4)
            coms=driver.find_elements_by_class_name('company_title')
            for c in coms:
                if c.text not in comli:
                    try:
                        sheet.write(index,0,c.text)
                        book.save('1.xls')
                        index+=1
                        notli.append(c.text)
                    except:
                        pass
            print('写入'+str(len(coms)))
            driver.execute_script(js)  
            sleep(2)
            cuurl=driver.current_url
            slindex=0
            while 1:
                try:
                    driver.find_elements_by_class_name('soupager__btn')[1].click()
                    if cuurl!=driver.current_url:break
                except:
                    sleep(1)
                slindex+=1
                if slindex>=5:break
            if cuurl == driver.current_url:break
        if len(notli)>0:
            win32api.MessageBox(0, "更新"+str(len(notli))+'家公司\n分别是'+str(notli), "提醒",win32con.MB_ICONASTERISK)
        else:
            print('没有更新公司')
        for j in notli:
            comli.append(j)
        sleep(120)
if __name__ == "__main__":
    main()