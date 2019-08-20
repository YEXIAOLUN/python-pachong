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
    url='https://search.51job.com/list/040000,000000,0000,00,9,99,%25E5%25A4%2596%25E8%25B4%25B8%25E4%25B8%259A%25E5%258A%25A1%25E5%2591%2598,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    driver.get(url)
    input('确认好相应的信息，然后按1爬取：')
    index =1
    while 1:
        js_top = "var q=document.documentElement.scrollTop=0"
        driver.execute_script(js_top)  
        sleep(2)
        table=driver.find_element_by_class_name('dw_table')
        coms=table.find_elements_by_class_name('el')
        for c in coms:
            try:
                cname=c.find_element_by_class_name('t2').text
                place=c.find_element_by_class_name('t3').text
                if place == '深圳-龙岗区':
                    print(place,cname)
                    sheet.write(index,0,cname)
                    book.save('前程无忧爬取公司.xls')
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
                driver.find_elements_by_class_name('bk')[1].click()
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
                driver.find_element_by_xpath('//input[@class="mytxt"]').clear()
                driver.find_element_by_xpath('//input[@class="mytxt"]').send_keys('1')
                o=driver.find_element_by_class_name('p_in')
                c=o.find_elements_by_css_selector('span')
                c[2].click()
                break
            except:
                pass
        notli=[]
        while 1:
            driver.execute_script(js_top)  
            sleep(4)
            table=driver.find_element_by_class_name('dw_table')
            coms=table.find_elements_by_class_name('el')
            for c in coms:
                if c.text not in comli:
                    cname=c.find_element_by_class_name('t2').text
                    place=c.find_element_by_class_name('t3').text
                    if place == '深圳-龙岗区':
                        try:
                            sheet.write(index,0,cname)
                            book.save('前程无忧爬取公司.xls')
                            index+=1
                            notli.append(cname)
                        except:
                            pass
            print('写入'+str(len(coms)))
            driver.execute_script(js)  
            sleep(2)
            cuurl=driver.current_url
            slindex=0
            while 1:
                try:
                    driver.find_elements_by_class_name('bk')[1].click()
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
