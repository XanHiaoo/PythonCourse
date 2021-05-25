#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time : 2021/5/25 
# @Author : XIAO
# @File : E11-3190421049-肖涵.py
import matplotlib.pyplot as plt
from scipy import optimize
from math import pi
from math import cos
import random
import numpy as np
import time
from collections import Counter

def f(x):
    return x*cos(x)
def getpoint(a,b):
    return random.uniform(a,b),random.uniform(0,b)

def listmethod(a,b,ponitsize,*args):
    start=time.perf_counter()
    cntin = 0
    cntout = 0
    pointin = []
    pointout = []

    for i in range(ponitsize):
        x1, y1 = getpoint(a, b)
        if (y1 <= f(x1)):
            pointin.append((x1, y1))
            cntin += 1
        else:
            pointout.append((x1, y1))
            cntout += 1
    cost = (time.perf_counter() - start)
    if(args):
        x = [i / 100 for i in range(0, 150 * b)]
        fy = [f(i) for i in x]
        Liner_plot, = plt.plot(x, fy, label="y=x+sin(x*pi*20)/80")
        plt.title('蒙特卡罗法求函数与x轴,x=a,x=b所围图形面积', fontproperties="SimHei", fontsize=15)
        plt.xlim((0.8 * a, 1.2 * b))
        plt.ylim((0, 1.1 * b))
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axvline(x=a, c="g", ls="--", lw=2, label="x=a")
        plt.axvline(x=b, c="g", ls="--", lw=2, label="x=b")
        plt.axhline(y=b, c="g", ls="--", lw=2, label="y=b")
        for point in pointin:
            plt.scatter(point[0], point[1], marker='*', color='plum')
        for point in pointout:
            plt.scatter(point[0], point[1], marker='x', color='lightskyblue')
        plt.show()

    area = (b - a) * b * cntin / (cntin + cntout)
    print('list方法————该所围图形面积约为：', area)
    print("list方法耗时:{}s".format(cost))
    return cost

def numpymethod(a,b,ponitsize):
    start = time.perf_counter()
    np.random.seed()
    x=np.random.uniform(a,b,ponitsize)
    y=np.random.uniform(0,b,ponitsize)
    fx=x*np.cos(x)
    y-=fx
    y = np.where(y > 0, 1, -1)
    cnt=Counter(y)
    area = (b - a) * b * cnt[-1] / ponitsize
    cost = (time.perf_counter() - start)
    print('numpy方法————该所围图形面积约为：', area)
    print("numpy方法耗时:{}s".format(cost))
    return cost

print("蒙特卡洛方法，采用1000个随机点计算函数在[a,b]区间内与x轴,x=6,x=66所围图形面积:")
a=6
b=66
listmethod(a,b,1000,True)
numpymethod(a,b,1000)
print("\n蒙特卡洛方法，采用10000000个随机点计算函数在[a,b]区间内与x轴,x=6,x=66所围图形面积,并测试numpy与list方法在大数据下的时间效率")
cost1=listmethod(a,b,1000000)
cost2=numpymethod(a,b,1000000)
print("numpy方法的效率大约是list方法的{}倍".format(cost1/cost2))

