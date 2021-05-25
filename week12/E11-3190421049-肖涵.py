#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time : 2021/6/1 
# @Author : XIAO
# @File : 3190421049-肖涵.py
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

image = Image.open('ntu.jpg')
image = np.array(image)
height=image.shape[0]
weight=image.shape[1]
print("\n该方法在图片转化为numpy数组后,在拼接黑色MASK放大尺寸。相比原方法：即在黑色numpy中绘图，在处理较大尺寸图片时，效率是原方法的1000倍左右\n")
cuttinghigh=int(input("请输入裁剪Height(原图Height:{}):".format(image.shape[0])))
cuttingweight=int(input("请输入裁剪Weight(原图Weight:{}):".format(image.shape[1])))
print("解析中……")
start=time.perf_counter()
if height%cuttinghigh:
    hcount=height//cuttinghigh+1
else:
    hcount = height // cuttinghigh
if weight%cuttingweight:
    wcount=weight//cuttingweight+1
else:
    wcount = weight // cuttingweight

mask1 = np.zeros([hcount*cuttinghigh-height,weight,3],dtype="uint8")
image=np.vstack((image,mask1))
mask2 = np.zeros([hcount*cuttinghigh,wcount*cuttingweight-weight,3],dtype="uint8")
image=np.hstack((image,mask2))
cost = (time.perf_counter() - start)
print("方法耗时:{}s".format(cost))
plt.imshow(image)
plt.show()

for i in range (0,hcount):
    for j in range(0,wcount):
        image_crop =image[i*cuttinghigh:(i+1)*cuttinghigh, j*cuttingweight:(j+1)*cuttingweight,:]
        txt='X'+str(i*cuttinghigh)+'Y'+str(j*cuttingweight)
        im_save = Image.fromarray(image_crop)
        im_save.save(txt+'.jpg')

