import torch
from matplotlib import animation
from torch.autograd import Variable
import matplotlib.pyplot as plt
import numpy as np
prea=[]
preb=[]
pred=[]
def init():
    aa = prea[1]
    bb = preb[1]
    dd = pred[1]
    x = np.arange(0, 100, 0.25)
    y = np.arange(0, 140, 0.25)
    X, Y = np.meshgrid(x, y)
    Z = aa * X + bb * Y + dd
    ax.plot_surface(X, Y, Z,
                    color='g',
                    alpha=0.6,
                    antialiased=True
                    )
    return ax.plot_surface
def updatesurface(num):
    for i in range(num):
        aa = prea[i]
        bb = preb[i]
        dd = pred[i]
        x = np.arange(0, 100, 0.25)
        y = np.arange(0, 140, 0.25)
        X, Y = np.meshgrid(x, y)
        Z = aa * X + bb * Y + dd
        ax.plot_surface(X, Y, Z,
                        color='g',
                        alpha=0.6
                        )

    return ax.plot_surface

if __name__ == '__main__':
    x = Variable(torch.linspace(0, 100).type(torch.FloatTensor))
    # Variable封装
    rand1 = Variable(torch.rand(100)) * 100
    y = x+rand1
    rand2 = Variable(torch.rand(100)) * 50
    z = x+rand2
    x_train = x[:-15]
    x_test = x[-15:]
    y_train = y[:-15]
    y_test = y[-15:]
    z_train = z[:-15]
    z_test = z[-15:]

    # matplotlib操作
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    plt.title("随机生成散点数据集", fontproperties="SimHei", fontsize=30)
    ax.scatter(x_train.data.numpy(), y_train.data.numpy(), z_train.data.numpy())
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

    a = Variable(torch.rand(1),requires_grad = True)
    b = Variable(torch.rand(1),requires_grad = True)
    d = Variable(torch.rand(1),requires_grad = True)
    learing_rate =0.00001
    losss=[]

    for i in range(1000):
        predictions=a.expand_as(x_train)*x_train+b.expand_as(x_train)*y_train+d.expand_as(x_train)
        prea.append(float(a.data))
        preb.append(float(b.data))
        pred.append(float(d.data))
        # expand转换成as()类型
        loss=torch.mean((predictions-z_train)**2)
        print("Loss rate:",loss.data)
        losss.append(loss)
        loss.backward()
        a.data.add_(- learing_rate * a.grad.data)
        b.data.add_(- learing_rate * b.grad.data)
        d.data.add_(- learing_rate * d.grad.data)
        a.grad.data.zero_()
        b.grad.data.zero_()
        d.grad.data.zero_()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    plt.title("平面拟合散点", fontproperties="SimHei", fontsize=30)
    ax.scatter(x_train.data.numpy(), y_train.data.numpy(), z_train.data.numpy())
    ax.scatter(x_test.data.numpy(), y_test.data.numpy(), z_test.data.numpy(),c='#DC143C')
    adata=float(a.data.numpy()[0])
    bdata = float(b.data.numpy()[0])
    ddata=float(d.data.numpy()[0])
    x = np.arange(0, 100, 0.25)
    y = np.arange(0, 140, 0.25)

    # 生成网格数据
    X, Y = np.meshgrid(x, y)
    Z = adata * X + bdata * Y + ddata
    ax.plot_surface(X,Y,Z,
                    color='g',
                    alpha=0.6
                    )
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.title("平面拟合过程3D演示", fontproperties="SimHei", fontsize=30)
    ax.scatter(x_train.data.numpy(), y_train.data.numpy(), z_train.data.numpy())
    ax.scatter(x_test.data.numpy(), y_test.data.numpy(), z_test.data.numpy(), c='#DC143C')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    sur_ani = animation.FuncAnimation(fig, updatesurface(10),np.arange(0,100),init_func=init(), interval=3000)
    plt.show()







