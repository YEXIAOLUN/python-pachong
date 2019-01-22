# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:27:36 2018
2
@author: Administrator
"""

import catchBaidu
import catch360
import catchZOL
import catchzhuti
import os
file='d://pictures'
folder = os.path.exists(file)
if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
	os.makedirs(file)            #makedirs 创建文件时如果路径不存在会创建这个路径
print('1:百度图片  2:360图片 ')
print('3:ZOL壁纸  4:电脑主题之家壁纸')
strs=input('请输入你要查找的图片壁纸网站')
if(strs=='4'):
    print('1:美食  2：小清新  3：植物  4：游戏  5：帅哥')
    print('6:汽车  7：美女  8：军事  9：家居  10：风景')
    strs2=input('请输入要查找的类型或直接选择快捷查找')
    words={'1':'美食','2':'小清新','3':'植物','4':'游戏','5':'帅哥',
           '6':'汽车','7':'美女','8':'军事','9':'家居','10':'风景'}
    word=words.get(strs2)
else:
    print('1:风景  2：动漫  3：美女  4：创意  5：卡通')
    print('6:汽车  7：游戏  8：可爱  9：明星  10：建筑')
    strs2=input('请输入要查找的类型或直接选择快捷查找')
    words={'1':'风景','2':'动漫','3':'美女','4':'创意','5':'卡通',
           '6':'汽车','7':'游戏','8':'可爱','9':'明星','10':'建筑'}
    if(words.get(strs2)==None):
        word=str(strs2)
    else:
        word=words.get(strs2)
size=int(input('输入你想获取的图片壁纸数量（最好不要太多）'))
if(strs=='1'):
    catchBaidu.main(word,size)
elif(strs=='2'):
    catch360.main(word,size)
elif(strs=='3'):
    catchZOL.main(word,size)
elif(strs=='4'):
    catchzhuti.main(word,size)
    