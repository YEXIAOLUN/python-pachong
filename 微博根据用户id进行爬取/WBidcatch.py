# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:38:57 2019

@author: Administrator
"""
import requests
import xlwt
import json
import datetime
import time
import bs4
import proxy_test
ids=input('请输入用户id')
stime=input('请输入要查找的开始时间')
etime=input('请输入要查找的结束时间')
stime = time.mktime(time.strptime(stime,'%Y-%m-%d-%H-%M'))
etime = time.mktime(time.strptime(etime,'%Y-%m-%d-%H-%M'))
url='http://m.weibo.cn/api/container/getIndex?type=uid&value='+str(ids)
pro=[]  #存储能用的ip地址
while(True):
    try:
        proxy,headers=proxy_test.main2()
        print(proxy)
        res=requests.get(url,headers=headers,proxies=proxy,timeout=2)
        pro.append(proxy)
        break
    except:
        pass
cid=json.loads(res.content)
cid=cid['data']['tabsInfo']['tabs'][1]['containerid']
#cid=1076032759348142
def dateTime(time):
    if('刚刚' in time):
        z=datetime.datetime.now()
        return z.strftime("%Y-%m-%d-%H-%M")
    if('秒前' in time):
        time=1
        z=datetime.datetime.now()-datetime.timedelta(minutes=int(time))
        return z.strftime("%Y-%m-%d-%H-%M")
    if('分钟前' in time):
        time=time.split('分钟前')[0]
        z=datetime.datetime.now()-datetime.timedelta(minutes=int(time))
        return z.strftime("%Y-%m-%d-%H-%M")
    if('小时前' in time):
        time=time.split('小时前')[0]
        z=datetime.datetime.now()-datetime.timedelta(minutes=int(time)*60)
        return z.strftime("%Y-%m-%d-%H-%M")
    if('昨天' in time):
        time=time.split('昨天 ')[1]
        time1=time.split(':')[0]
        time2=time.split(':')[1]
        z=datetime.datetime.now()-datetime.timedelta(minutes=2*60*12)
        return z.strftime("%Y-%m-%d")+'-'+str(time1)+'-'+str(time2)
    if(len(time)>5):
        return time+'-00-00'
    return '2019-'+time+'-00-00'
def info(jsons,i,times):
    dian=jsons['data']['cards'][i]['mblog']['reposts_count']
    comment=jsons['data']['cards'][i]['mblog']['comments_count']
    zhuan=jsons['data']['cards'][i]['mblog']['attitudes_count']
    urls=jsons['data']['cards'][i]['scheme']
    try:
        iszhuan=jsons['data']['cards'][i]['mblog']['retweeted_status']
        iszhuan=jsons['data']['cards'][i]['mblog']['retweeted_status']['text']
        try:
            picnum=len(jsons['data']['cards'][i]['mblog']['retweeted_status']['pics'])
        except:
            picnum=0
        try:
            video=jsons['data']['cards'][i]['mblog']['retweeted_status']['page_info']['media_info']['stream_url']
        except:
            video='Null'
    except:
        iszhuan=False
        try:
            picnum=len(jsons['data']['cards'][i]['mblog']['pics'])
        except:
            picnum=0
        try:
            video=jsons['data']['cards'][i]['mblog']['page_info']['media_info']['stream_url']
        except:
            video='Null'
    l=[]
    text=jsons['data']['cards'][i]['mblog']['text']
    bs=bs4.BeautifulSoup(text,'lxml')
    text=bs.text
    imgs=bs.findAll('img')
    if len(imgs)==0:
        imgsurl='Null'
    else:
        imgsurl=''
        for i in imgs:
            try:
                imgsurl+=i.get_attribute_list('alt')[0]
            except:
                pass
    if imgsurl=='':
        imgsurl='Null'
    aurl=bs.findAll('a')
    huati=''
    isate=''
    for i in aurl:
        if '#' in i.text:
            huati+=i.text
        if '@' in i.text:
            isate+=i.text
    if huati=='':
        huati='Null'
    if isate=='':
        isate='Null'
    l.append(times)
    l.append(text)
    l.append(imgsurl)
    l.append(huati)
    l.append(isate)
    l.append(dian)
    l.append(comment)
    l.append(zhuan)
    l.append(iszhuan)
    l.append(picnum)
    l.append(video)
    l.append(urls)
    return l
def con(url2):
    if len(pro)!=0:
        for i in pro:
            proxy=i
            headers=proxy_test.gethea()
            try:
                res=requests.get(url2,headers=headers,proxies=proxy,timeout=1.5)
                return res
            except:
                pass
        while(True):
            proxy,headers=proxy_test.main2()
            #print('proxy2',proxy)
            try:
                res=requests.get(url2,headers=headers,proxies=proxy,timeout=3)
                pro.append(proxy)
                return res
            except:
                pass
def main():
    lists=[]
    page=470
    boo=True
    while(boo):
        url2='http://m.weibo.cn/api/container/getIndex?type=uid&value='+str(ids)+'&containerid='+str(cid)+'&page='+str(page)
        res=con(url2)
        try:
            jsons=json.loads(res.text)
        except:
            continue
        num=len(jsons['data']['cards'])
        for i in range(0,num):
            try:
                times=dateTime(jsons['data']['cards'][i]['mblog']['created_at'])
            except:
                continue
            print(times)
            times2= time.mktime(time.strptime(times,'%Y-%m-%d-%H-%M'))
            if(times2-stime<0):
                try:
                    if jsons['data']['cards'][i]['mblog']['isTop']==1:
                        continue
                except:
                    pass
                boo=False
                break
            if(times2-etime<=0):
                lists.append(info(jsons,i,times))
        page+=1
    xieru(lists)
def xieru(lists):
    book = xlwt.Workbook()
    sheet = book.add_sheet('weibo')
    sheet.write(0,1,'发布时间')
    sheet.write(0,2,'微博内容')
    sheet.write(0,3,'是否有表情')
    sheet.write(0,4,'是否有话题')    
    sheet.write(0,5,'是否@')
    sheet.write(0,6,'点赞数')
    sheet.write(0,7,'分享数')
    sheet.write(0,8,'评论数')
    sheet.write(0,9,'是否转发')
    sheet.write(0,10,'是否有图片')
    sheet.write(0,11,'是否有视频')
    sheet.write(0,12,'微博链接')
    index=0
    for i,j in enumerate(lists):
        sheet.write(i+1,0,index)
        sheet.write(i+1,1,j[0])
        sheet.write(i+1,2,j[1])
        sheet.write(i+1,3,j[2])
        sheet.write(i+1,4,j[3])
        sheet.write(i+1,5,j[4])
        sheet.write(i+1,6,j[5])
        sheet.write(i+1,7,j[6])
        sheet.write(i+1,8,j[7])
        sheet.write(i+1,9,j[8])
        sheet.write(i+1,10,j[9])
        sheet.write(i+1,11,j[10])
        sheet.write(i+1,12,j[11])
        index+=1
    book.save('d://weibos.xlsx')
if __name__=="__main__":
    main()
