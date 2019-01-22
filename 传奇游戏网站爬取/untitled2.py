# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:39:58 2019

@author: Administrator
"""

import requests
import bs4
import json
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

def geturl():
    url='http://mxjt2019.ue1q6.top:823/?'
    res=requests.get(url,headers=header)

    bs=bs4.BeautifulSoup(res.content,'html.parser')
    cl=bs.findAll(class_='c7')
    a=[]
    for i in range(0,len(cl)):
        try:
            a.append(cl[i].find('a').get_attribute_list('href')[0])
        except:
            pass
    a2=list(set(a))
    return a2
def xiazaiurl(url):
    f=open('d://游戏下载链接1.txt','w',encoding='utf8')
    a2=url
    for z in a2:
        baiduyun=[]
        lanzous=[]
        yun360=[]
        weiyun=[]
        file=[]
        try:
            dowload=[]
            res2=requests.get(z,headers=header,timeout=0.1)
            bs11=bs4.BeautifulSoup(res2.content,'lxml')
            title=bs11.find('title').text
            print(bs11.find('title').text+'    链接：' +z+'\n')
            aa=bs11.findAll('a')
            for i in aa:
                try:
                    if ('下载' in i.text or i.find('img') or '下载' in i.get_attribute_list('title')[0]) and i.get_attribute_list('href')[0] != None and '#' not in i.get_attribute_list('href')[0]:
                        dowload.append(i.get_attribute_list('href')[0])
                except:
                    pass
            dowload=list(set(dowload))
            for i in dowload:
                u=z+'/'+i
                if(u[-3:]=='rar' or u[-3:]=='zip' or u[-3:]=='exe'):
                    file.append(u)
                    continue
                r=requests.get(u,headers=header,timeout=0.1)
                b=bs4.BeautifulSoup(r.content,'lxml')
                m=b.findAll('a')
                for j in m:
                    if '下载' in j.text:
                        if 'http' not in j.get_attribute_list('href')[0]:
                            urlfile=u+j.get_attribute_list('href')[0]
                        else:
                            urlfile=j.get_attribute_list('href')[0]
                        if 'pan.baidu' in urlfile:
                            baiduyun.append(urlfile)
                        elif 'lanzous' in urlfile:
                            lanzous.append(urlfile)
                        elif 'yunpan.360' in urlfile:
                            yun360.append(urlfile)
                        elif 'weiyun' in urlfile:
                            weiyun.append(urlfile)
            baiduyun=list(set(baiduyun))
            lanzous=list(set(lanzous))
            yun360=list(set(yun360))
            weiyun=list(set(weiyun))
            file=list(set(file))
            game={
                    'title':title,
                    'urls':z,
                    'baiduyun':baiduyun,
                    'lanzous':lanzous,
                    'yun360':yun360,
                    'weiyun':weiyun,
                    'file':file
                    }
            f.write(json.dumps(game))
            f.flush()
        except:
            pass
    f.close()

if __name__ == "__main__":
    pass
    #url=geturl()
    #xiazaiurl(url)