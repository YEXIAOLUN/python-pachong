# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:06:57 2018

@author: Administrator
"""
from sinaInfo import sinaInfo
from levelStat import levelStat
class pageInfo:
    userInfo = 0#作者的数据
    deep=0          #到达两百篇文章时，文章的最大深度
    speed=0         #到达两百篇文章时，耗费的时间
    level = [levelStat(),levelStat(),levelStat(),levelStat(),levelStat(),levelStat(),levelStat()]#具体统计的信息
    sendInfo = []      #用来存放每一个级联的数据(其中包含着很多的用户信息)

    def __init__(self):
        pass
    #[[作者， 链接， 深度， 速度， 作者的信息， 转发用户的信息]]
    
             
