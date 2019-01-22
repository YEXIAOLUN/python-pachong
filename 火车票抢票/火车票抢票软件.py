from selenium import webdriver
from selenium.webdriver.common.keys import *
from time import sleep
import bs4
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.12306.cn/mormhweb/')
sleep(3)
driver.find_element_by_xpath('//img[@src="./images/newS.gif"]').click()
sleep(3)
driver.switch_to_window(driver.window_handles[-1])
chufa="//input[@name='leftTicketDTO.from_station_name']"
mudi="//input[@name='leftTicketDTO.to_station_name']"
rqi="//div[text()='国庆']"
while(True):
    try:
        driver.find_element_by_xpath(chufa).clear()
        driver.find_element_by_xpath(chufa).send_keys('杭州')
        sleep(1)
        driver.find_element_by_xpath(chufa).send_keys(Keys.ENTER)
        driver.find_element_by_xpath(mudi).clear()
        driver.find_element_by_xpath(mudi).send_keys('上海')
        sleep(1)
        driver.find_element_by_xpath(mudi).send_keys(Keys.ENTER)
        driver.find_element_by_id('train_date').click()
        driver.find_element_by_xpath(rqi).click()
        break
    except:
        driver.refresh()
driver.find_element_by_id('a_search_ticket').click()
sleep(3)
text=driver.page_source
bs=bs4.BeautifulSoup(text,'lxml')
tickets=bs.select('#queryLeftTable')
print(tickets)
