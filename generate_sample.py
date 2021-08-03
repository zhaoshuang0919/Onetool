# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:05:37 2021

@author: zhi
"""
hello

from PIL import Image,ImageFont,ImageDraw
import os
import random
import re

def w2p(te, zt,i):
    #待变换字符
    text = te
    #text = u"ABCD"
    #画布尺寸coco数据集大小
    width = 640
    height = 360
    im = Image.new("RGB", (width, height), (255, 255, 255)) # 图像大小与背景颜色
    dr = ImageDraw.Draw(im)
    
    #设置字体
    #font = ImageFont.truetype(os.path.join("", "msyh.ttc"), 70) # 字体与字大小
    font = ImageFont.truetype(os.path.join("D:\zhaoshuang\生成项目\数据集\字体", zt), 90) # 字体与字大小#中文70英文90
    #调整居中
    w, h = font.getsize(text)
    dr.text(((width-w)/2, (height-h)/2), text, font=font, fill="#000000") # 字位置与字颜色
    
    #im.show()
    
    im.save(r"D:\zhaoshuang\生成项目\数据集\datasete1\ "+te+str(i)+ ".jpg") # 保存
    
def english():
    res = []
    file = open("D:\zhaoshuang\生成项目\数据集\字体\english.txt") 
    while 1:
        lines = file.readlines(100000)
        if not lines:
          break
        for line in lines:
            res.append(line.strip('\n'))
    file.close()
    #随机选取3-10个字母
    num = random.randint(3,10) 
    values = random.sample(res, num)
    text = ''.join(values)
    return text

def chinese():
    sourceFile = open('D:\zhaoshuang\生成项目\数据集\字体\gen_name\source.txt', encoding='utf-8')

    Source = set(''.join(sourceFile.readlines()))
    sourceFile.close()
    
    ChineseChars = list([c for c in Source if re.match(r'[^…\\\/\"\'0-9A-Za-z_\-\s+=*/~`,.?!@#$%&*\(\)\|<>！￥（）—-“‘’”，。？：；]', c) ])
    Count = len(ChineseChars)
    #print(Count, len(Source))
    num = random.randint(3,8) 
    values = random.sample(ChineseChars, num)
    text = ''.join(values)
    return text
'''
#生成中文数据集8种字体，每种200张，共1600张
for i in range(0,1600,8):
    text = chinese()
    #print(text)
    w2p(text,"msyh.ttc",i)
    w2p(text,"msyhbd.ttc",i+1)
    w2p(text,"msyhl.ttc",i+2)
    w2p(text,"汉仪凌波体简.ttf",i+3)
    w2p(text,"邓玉二笔体.ttf",i+4)
    w2p(text,"落落の汤圆.ttf",i+5)
    w2p(text,"迷你简流行体.ttf",i+6)
    w2p(text,"喵小姐简体.ttf",i+7)

#text = chinese()
#print(text)
#w2p(text,"msyh.ttc")

'''
#生成英文数据集10种字体，每种200张，共2000张
for i in range(0,2000,10):
    text = english()
    #print(text)
    w2p(text,"arial.ttf",i)
    w2p(text,"arialbd.ttf",i+1)
    w2p(text,"arialbi.ttf",i+2)
    w2p(text,"ariali.ttf",i+3)
    w2p(text,"ariblk.ttf",i+4)
    w2p(text,"汉仪凌波体简.ttf",i+5)
    w2p(text,"邓玉二笔体.ttf",i+6)
    w2p(text,"落落の汤圆.ttf",i+7)
    w2p(text,"迷你简流行体.ttf",i+8)
    w2p(text,"喵小姐简体.ttf",i+9)

    
    
    
    
    
    
    

