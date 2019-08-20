from selenium import webdriver
import xlwt
from time import sleep
def main():
    pass

def get(filename):
    book = xlwt.Workbook()
    sheet = book.add_sheet('Sheet1')
    an=driver.find_elements_by_class_name('hideBtn')
    for a in an:
        a.click()
        sleep(0.2)
    text=driver.find_elements_by_class_name('text')
    title=driver.find_elements_by_class_name('c_title')
    index=0
    sin=driver.find_elements_by_class_name('c_sinSelect')
    num=driver.find_elements_by_class_name('c_mutSelect')
    for s in sin:
        lis=s.find_elements_by_css_selector('li')
        sheet.write(index,0,title[index].text)
        sheet.write(index,1,lis[ord(text[index].text.split(' ')[1])-65].text)
        book.save(filename+'.xls')
        index+=1
    for n in num:
        lis=n.find_elements_by_css_selector('li')
        sheet.write(index,0,title[index].text)
        ans=text[index].text.split(' ')[1].split(',')
        col=1
        for a in ans:
            sheet.write(index,col,lis[ord(a)-65].text)
            col+=1
            book.save(filename+'.xls')
        index+=1
    for i in range(index,len(title)):
        sheet.write(i,0,title[i].text)
        sheet.write(i,1,text[i].text.split(' ')[1])
        book.save(filename+'.xls')
if __name__ == "__main__":
    pass
