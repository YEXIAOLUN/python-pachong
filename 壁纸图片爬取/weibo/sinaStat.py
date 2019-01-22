# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 16:06:57 2018

@author: Administrator
"""
class levelStat:        #每篇文章的级联统计
    ageCnt = [0 for i in range(10)] #每10岁一个阶段
    bigvCnt = 0
    provinceDirt= {}
    levelCnt = [0 for i in range(6)] #每8级一个阶段
    level = 0   #转发级层  0表示创作者，1表示第一次转发，2表示第二次转发
    Info = []   #用来存放每一个级联的文章 sinaInfo添加放入
    
    def __init__(self, level):
        self.level = level;
        
    def ageStat(self, age):
        self.ageCnt[age // 10] = self.ageCnt[age // 10] + 1
        
    def bigvStat(self, isBigv):
        if(isBigv):
            self.bigvCnt = self.bigvCnt + 1
    
    def provinceStat(self, value):#如果不包含该省份，则将省份加入变量内，否则+1
        if value not in self.provinceDirt.keys():
            self.provinceDirt[value] = 0
        else:
            self.provinceDirt[value] = self.provinceDirt[value] + 1
        
    def levelStat(self, level):
        self.ageCnt[level // 8] = self.ageCnt[level // 8] + 1
    
    def addInfo(self, sinaInfo): #
        self.Info.append(sinaInfo)
        
        
class sinaInfo:
    userName=''  #用户名
    pageLink=''  #主页链接
    sex=''	   #性别
    age=''	   #转发用户年龄
    isBigv=False    #是否大V
    province=''  #来自的省份
    level=0     #转发级层  0表示创作者，1表示第一次转发，2表示第二次转发
    content=''   #转发内容	
    sendCnt=0   #转发数
    talkCnt=0   #评论数
    goodCnt=0   #点赞数
    
    def __init__(self, author, link, userName, pageLink, sex, age, isBigv, province, content, sendCnt, talkCnt, goodCnt):
        self.author = author
        self.link = link
        self.userName = userName
        self.pageLink = pageLink
        self.sex = sex
        self.age = age
        self.isBigv = isBigv
        self.province = province
        self.content = content
        self.sendCnt = sendCnt
        self.talkCnt = talkCnt
        self.goodCnt = goodCnt


class page_info:
    author=''	   #文章作者
    link=''	   #文章链接
    sinaInfo = sinaInfo()
    level1 = levelStat(1)
    level2 = levelStat(2);


   

        #for i in range(0, 100, 10):
            
     
