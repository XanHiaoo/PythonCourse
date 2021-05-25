import matplotlib
import matplotlib.pyplot as plt
import math
from math import pi
from math import sin
import time
def Liner(x):
    return x
def EarlyPause(x):
    return (x+(1-sin(x*pi*2+pi/2))/(-8))
def LatePause(x):
    return (x+(1-sin(x*pi*2+pi/2))/8)
def SlowWavy(x):
    return (x+sin(x*pi*5)/20)
def FastWavy(x):
    return (x+sin(x*pi*20)/80)
def Power(x):
    return pow(x+(1-x)*0.03,2)
def InversePower(x):
    return (1+pow((1-x),1.5)*-1)
def FastPower(x):
    return pow((x+(1-x)/2),8)
def InverseFastPower(x):
    return (1+pow((1-x),3)*-1)
if __name__ == '__main__':
    plt.figure(figsize=(8,8))  # 设置坐标轴的大小
    plt.title("进度条显示", fontproperties="SimHei", fontsize=30)
    plt.xlim((0, 1))
    plt.ylim((0, 1))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xticks([0,0.2,0.4,0.6,0.8,1],['0%','20%','40%','60%','80%','100%'])
    plt.yticks([0.2,0.4,0.6,0.8,1],['20%','40%','60%','80%','100%'])

    x=[i/100 for i in range(0,101,1)]
    Liner_y=[Liner(i) for i in x]
    EarlyPause_y=[EarlyPause(i) for i in x]
    LatePause_y=[LatePause(i) for i in x]
    SlowWavy_y=[SlowWavy(i) for i in x]
    FastWavy_y=[FastWavy(i) for i in x]
    Power_y=[Power(i) for i in x]
    InversePower_y=[InversePower(i) for i in x]
    FastPower_y=[FastPower(i) for i in x]
    InverseFastPower_y=[InverseFastPower(i) for i in x]

    Liner_plot,=plt.plot(x,Liner_y)
    EarlyPause_plot,=plt.plot(x, EarlyPause_y)
    LatePause_plot,=plt.plot(x, LatePause_y)
    SlowWavy_plot,=plt.plot(x,SlowWavy_y)
    FastWavy_plot,=plt.plot(x, FastWavy_y)
    InversePower_plot,=plt.plot(x, InversePower_y)
    FastPower_plot,=plt.plot(x, FastPower_y)
    InverseFastPower_plot,=plt.plot(x, InverseFastPower_y)
    plt.legend([Liner_plot,EarlyPause_plot,LatePause_plot,SlowWavy_plot,FastWavy_plot,InversePower_plot,FastPower_plot,InverseFastPower_plot],
                      ['Liner','EarlyPause','LatePause','SlowWavy','FastWavy','InversePower','FastPower','InverseFastPower']
                      )
    plt.show()

    scale=int(input("---时间总长度设置为100，请输入在[0-100]范围内需要显示的整数时间点--:"))
    c=scale
    start = time.perf_counter()
    scale/=100
    for i in range(c+1):
        Liner_a, Liner_b = '*' * int(Liner(i/100) * 100), '.' * (100 - int(Liner(i/100) * 100))
        print("\r{:^3.0f}%[{}->Loading{}]Liner".format(Liner(scale)*100, Liner_a, Liner_b),end='')
        time.sleep(0.02)
    print('\n')
    for i in range(c + 1):
        EarlyPause_a, EarlyPause_b = '*' * int(EarlyPause(i/100) * 100), '.' * (100 - int(EarlyPause(i/100) * 100))
        print("\r{:^3.0f}%[{}->Loading{}]EarlyPause".format(EarlyPause(scale) * 100, EarlyPause_a, EarlyPause_b),end='')
        time.sleep(0.02)
    print('\n')
    for i in range(c + 1):
        LatePause_a, LatePause_b = '*' * int(LatePause(i/100) * 100), '.' * (100 - int(LatePause(i/100) * 100))
        print("\r{:^3.0f}%[{}->Loading{}]LatePause".format(LatePause(scale) * 100, LatePause_a, LatePause_b),end='')
        time.sleep(0.02)
    print('\n')
    for i in range(c + 1):
        SlowWavy_a, SlowWavy_b = '*' * int(SlowWavy(i/100) * 100), '.' * (100 - int(SlowWavy(i/100) * 100))
        print("\r{:^3.0f}%[{}->Loading{}]SlowWavy".format(SlowWavy(scale) * 100, SlowWavy_a, SlowWavy_b),end='')
        time.sleep(0.02)
    print('\n')
    for i in range(c + 1):
        FastWavy_a, FastWavy_b = '*' * int(FastWavy(i/100) * 100), '.' * (100 - int(FastWavy(i/100) * 100))
        print("\r{:^3.0f}%[{}->Loading{}]FastWavy".format(FastWavy(scale) * 100,FastWavy_a, FastWavy_b),end='')
        time.sleep(0.02)
    print('\n')
    for i in range(c + 1):
        Power_a, Power_b = '*' * int(Power(i/100) * 100), '.' * (100 - int(Power(i/100) * 100))
        print("\r{:^3.0f}%[{}->Loading{}]Power".format(Power(scale) * 100, Power_a, Power_b),end='')
        time.sleep(0.02)
    print('\n')
    for i in range(c + 1):
        InversePower_a, InversePower_b = '*' * int(InversePower(i/100) * 100), '.' * (100 - int(InversePower(i/100) * 100))
        print("\r{:^3.0f}%[{}->Loading{}]InversePower".format(InversePower(scale) * 100, InversePower_a, InversePower_b),end='')
        time.sleep(0.02)
    print('\n')
    for i in range(c + 1):
        FastPower_a, FastPower_b = '*' * int(FastPower(i/100) * 100), '.' * (100 - int(FastPower(i/100) * 100))
        print("\r{:^3.0f}%[{}->Loading{}]FastPower".format(FastPower(scale) * 100, FastPower_a, FastPower_b),end='')
        time.sleep(0.02)
    print('\n')
    for i in range(c + 1):
        InverseFastPower_a, InverseFastPower_b = '*' * int(InverseFastPower(i/100) * 100), '.' * (100 - int(InverseFastPower(i/100) * 100))
        print("\r{:^3.0f}%[{}->Loading{}]InverseFastPower".format(InverseFastPower(scale) * 100, InverseFastPower_a, InverseFastPower_b),end='')
    time.sleep(0.02)






