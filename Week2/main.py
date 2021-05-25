import torch
from torch.autograd import Variable
import matplotlib.pyplot as plt
import numpy as np
if __name__ == '__main__':
    x = Variable(torch.linspace(0, 100).type(torch.FloatTensor))
    rand = Variable(torch.rand(100)) * 100
    y = x + rand
    x_train = x[:-10]
    x_test = x[-10:]
    y_train = y[:-10]
    y_test = y[-10:]
    plt.figure(figsize=(10, 8))
    plt.title("随机生成的训练数据集",fontproperties="SimHei",fontsize=50)
    plt.plot(x_train.data.numpy(), y_train.data.numpy(), 'o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

    a = Variable(torch.rand(1),requires_grad = True)
    b = Variable(torch.rand(1), requires_grad=True)
    learing_rate =0.0001
    losss=[]
    prea=[]
    preb=[]
    for i in range(100):
        prea.append(a.data)
        preb.append(b.data)
        predictions=a.expand_as(x_train)*x_train+b.expand_as(x_train)
        loss=torch.mean((predictions-y_train)**2)
        print("Loss rate:",loss.data)
        losss.append(loss)
        loss.backward()
        a.data.add_(- learing_rate * a.grad.data)
        b.data.add_(- learing_rate * b.grad.data)
        a.grad.data.zero_()
        b.grad.data.zero_()
    x_data=x_train.data.numpy()
    plt.figure(figsize=(10,8))
    xplot,=plt.plot(x_data,y_train.data.numpy(),'o')
    yplot,=plt.plot(x_data,a.data.numpy()[0]*x_data+b.data.numpy()[0])
    plt.xlabel('X')
    plt.ylabel('Y')
    str1=str(a.data.numpy()[0])+'x'+str(b.data.numpy()[0])
    plt.legend([xplot,yplot],['Data',str1])
    plt.show()
    print(prea)
    print(preb)


    predictions=a.expand_as(x_test)*x_test+b.expand_as(x_test)
    print('predictions:',predictions.data)

    x_data=x_train.data.numpy()
    x_pred=x_test.data.numpy()
    plt.figure(figsize=(10,8))
    plt.plot(x_data,y_train.data.numpy(),'o')
    plt.plot(x_pred,y_test.data.numpy(),'s')
    x_data=np.r_[x_data,x_test.data.numpy()]
    plt.plot(x_data,a.data.numpy()*x_data+b.data.numpy())
    plt.plot(x_pred,a.data.numpy()*x_pred+b.data.numpy(),'o')
    plt.xlabel('X')
    plt.ylabel('Y')
    str1 = str(a.data.numpy()[0]) + 'x' + str(b.data.numpy()[0])
    plt.legend([xplot, yplot], ['Data', str1])
    plt.show()




