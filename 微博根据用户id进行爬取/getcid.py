# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:54:36 2019

@author: Administrator
"""

import json
import requests
import proxy_test
ids=input('请输入用户id')
page=1
pro=[]  #存储能用的ip地址
url='http://m.weibo.cn/api/container/getIndex?type=uid&value='+str(ids)
while(True):
    try:
        proxy,headers=proxy_test.main2()
        res=requests.get(url,headers=headers,proxies=proxy,timeout=2)
        pro.append(proxy)
        break
    except:
        pass
cid=json.loads(res.content)
cid=cid['data']['tabsInfo']['tabs'][1]['containerid']
url2='http://m.weibo.cn/api/container/getIndex?type=uid&value='+str(ids)+'&containerid='+str(cid)+'&page='+str(page)
print(url2)