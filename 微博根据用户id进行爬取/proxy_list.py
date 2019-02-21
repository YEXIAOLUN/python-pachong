# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:56:40 2019

@author: YEXIAOLUN
"""

import json
import telnetlib
import requests

proxy_url = 'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list'
# proxyList = []
f=open('verified_proxies.json','a+')
num=50  #设置代理地址数量
def verify(ip,port,types,index):
    proxies = {}
    try:
        telnetlib.Telnet(ip,port=port,timeout=3)
    except:
        print('unconnected')
        return False
    else:
        proxies['type'] = types
        proxies['host'] = ip
        proxies['port'] = port
        proxiesJson = json.dumps(proxies)
        if index<num:
            f.write(proxiesJson + ',\n')
        else:
            f.write(proxiesJson + '\n')
        print("已写入：%s" % proxies)
        return True

def getProxy(proxy_url):
    response = requests.get(proxy_url)
    proxies_list = response.text.split('\n')
    index=1
    f.write('[')
    for proxy_str in proxies_list:
        proxy_json = json.loads(proxy_str)
        host = proxy_json['host']
        port = proxy_json['port']
        types = proxy_json['type']
        if verify(host,port,types,index):
            index+=1
        if index>num:
            break
    f.write(']')
    f.close()

if __name__ == '__main__':
    getProxy(proxy_url)

