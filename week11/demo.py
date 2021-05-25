import numpy as np
from PIL import Image
# im=Image.open('yong.jpg')
# print(np.array(im))
# print(np.array(im).shape)
# im.show()


# import numpy as np
# np.random.seed(12345)#seed( ) 用于指定随机数生成时所用算法开始的整数值，如果使用相同的seed( )值，则每次生成的随即数都相同
#
# nsteps = 1000
# draws = np.random.randint(0, 2, size=nsteps)#函数的作用是，返回一个随机整型数,即[low, high)。
# steps = np.where(draws > 0, 1, -1)#满足条件(condition)，输出x，不满足输出y
#
# walk = steps.cumsum()#返回沿给定轴的元素的累加和。
# print(walk)
#
# print(walk.min())
# print(walk.max())
# max=(np.abs(walk) >= 10).argmax()#argmax返回的是最大数的索引
# print(max)
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 输出随机数的尺寸，比如size = (m, n, k)，则输出数组的shape = (m, n, k)
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)#按行累加
walks
# plt.plot(walk[:100])
# plt.show()
print(walks.max())
print(walks.min())
hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)
print(hits30.sum()) # Number that hit 30 or -30
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
crossing_times.mean()
steps = np.random.normal(loc=0, scale=0.25,
                         size=(nwalks, nsteps))
print(steps)