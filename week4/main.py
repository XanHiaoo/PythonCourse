import matplotlib.pyplot as plt
from scipy import optimize
from math import pi
from math import cos
import random
import numpy as np
def f(x):
    return x*cos(x)
def getpoint(a,b):
    return random.uniform(a,b),random.uniform(0,b)
def main():
    plt.figure(figsize=(8, 8))  # 设置坐标轴的大小
    plt.title("f(x)=x*cosx函数图像展示", fontproperties="SimHei", fontsize=30)
    plt.xlim((0, 100))
    plt.ylim((0, 100))
    plt.xlabel('X')
    plt.ylabel('Y')
    x = [i / 100 for i in range(0, 10001)]
    fy = [f(i) for i in x]
    Liner_plot, = plt.plot(x, fy, label="y=xcos(x)")
    plt.show()

    print("请选择正整数[a,b]区间,用于计算函数在[a,b]区间内与x轴,x=a,x=b所围图形面积，例如[6,66]")
    a = int(input('a = '))
    b = int(input('b = '))
    if (a > b):
        print('区间输入有误，请重新启动程序')
    # maximum = optimize.fminbound(lambda x: -f(x), a, b)

    plt.title('蒙特卡罗法求函数与x轴,x=a,x=b所围图形面积', fontproperties="SimHei", fontsize=15)
    plt.xlim((0.8 * a, 1.2 * b))
    plt.ylim((0, 1.1 * b))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axvline(x=a, c="g", ls="--", lw=2, label="x=a")
    plt.axvline(x=b, c="g", ls="--", lw=2, label="x=b")
    plt.axhline(y=b, c="g", ls="--", lw=2, label="y=b")

    x = [i / 100 for i in range(0, 150 * b)]
    fy = [f(i) for i in x]
    Liner_plot, = plt.plot(x, fy, label="y=x+sin(x*pi*20)/80")
    cntin = 0
    cntout = 0
    pointin = []
    pointout = []

    for i in range(3000):
        x1, y1 = getpoint(a, b)
        if (y1 <= f(x1)):
            pointin.append((x1, y1))
            cntin += 1
        else:
            pointout.append((x1, y1))
            cntout += 1
    for point in pointin:
        plt.scatter(point[0], point[1], marker='*', color='plum')
    for point in pointout:
        plt.scatter(point[0], point[1], marker='x', color='lightskyblue')
    x1, y1 = getpoint(a, b)
    plt.scatter(point[0], point[1], marker='*', color='plum', label='point_in_area')
    plt.scatter(point[0], point[1], marker='x', color='lightskyblue', label='point_out_area')

    plt.legend()
    plt.show()
    area = (b - a) * b * cntin / (cntin + cntout)
    print('该所围图形面积约为：', area)
    print("当做一测试，使得区间为[5,7],得到用该法求得面积值为 9.8784，经实际积分计算值为9.863767633227296")

main()

