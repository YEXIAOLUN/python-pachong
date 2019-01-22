from selenium import webdriver
from time import sleep
import requests
import os
from moviepy.editor import VideoFileClip
driver=webdriver.PhantomJS()
driver.maximize_window()
driver.get('http://mooc.icve.com.cn/')
driver.switch_to_window(driver.window_handles[1])
driver.close()
driver.switch_to_window(driver.window_handles[0])
sleep(3)
print('正在登陆')
driver.find_element_by_link_text('登录').click()
driver.find_element_by_name('userName').send_keys('20172030208')
driver.find_element_by_name('userPwd').send_keys('666666')
print('进入学习选择页面')
sleep(2)
driver.find_element_by_link_text('立即登录').click()
sleep(1)
driver.find_element_by_link_text('个人中心').click()
sleep(1)
driver.find_element_by_class_name('mc-lesson-cover').click()
sleep(1)
driver.find_element_by_link_text('课程学习').click()
sleep(1)
print('正在进入需要学习的课程')
list1=[]
while(len(list1)<3):
        driver.find_element_by_xpath("//span[@title='初识Java语言']").click()
        unit1=driver.find_element_by_class_name('moduleList')
        list1=unit1.text.split('\n')
list1=[i.strip() for i in list1]
unittext1=list1[0]
list1=list1[2:]
list2=[]
for i,j in enumerate(list1):
	try:
		if int(j)>0:
			list2.append(list1[i+1])
	except:
		list2=list2
print('第一块内容',unittext1)
print(list2)
def click():
    for i in list2:
        lists=[]
        a=driver.find_element_by_xpath("//a[@title='"+i+"']/../../../../..")
        lists=a.text.split('\n')
        if(len(lists)==1):
            driver.find_element_by_link_text(lists[0]).click()
click()
url=driver.current_url
def ec():
    try:
        driver.switch_to_alert().accept()
    except:
        sleep(0)
for i in list2:
    lists=[]
    a=driver.find_element_by_xpath("//a[@title='"+i+"']/../../../../..")
    lists=a.text.split('\n')
    listss=[]
    for j in lists:
        if listss.count(j)<1:
            listss.append(j)
    print(listss)
    listss=listss[1:]
    for z in listss:
        lista=driver.find_elements_by_link_text(z)
        for k in range(0,len(lista)):
            lista=driver.find_elements_by_link_text(z)
            sleep(2)
            print(lista[k].text)
            lista[k].click()
            sleep(2)
            if (len(driver.window_handles))>1:
                    print('作业页面，即将关闭')
                    driver.switch_to_window(driver.window_handles[1])
                    #driver.find_elements_by_link_text('做测验').click()
                    driver.close()
                    ec()
                    driver.switch_to_window(driver.window_handles[0])
            elif (driver.current_url!=url):
                    try:
                        shipin=driver.find_element_by_xpath("//video").get_attribute('src')
                        res=requests.get(shipin)
                        file='d://shipin.mp4'
                        print('正在刷取视频，请等待'+lista[k].text)
                        f=open(file,'wb')
                        f.write(res.content)
                        times=VideoFileClip(file).duration
                        os.remove(file)
                        sleep(times)
                    except:
                        sleep(0)
                    driver.back()
                    ec()
                    sleep(1)
                    click()
                    sleep(1)
            else:
                    sleep(0)
