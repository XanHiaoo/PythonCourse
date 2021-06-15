# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 13:11
# @Author  : Han
# @File    : main.py
import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pylab as mpl

# 读入数据文件，第一行为数据
from mpl_toolkits.mplot3d import Axes3D
names=['class', 'Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']
df_wines = pd.read_csv('./wine.data', header=None, names=names)
print(df_wines.head(5))



array = df_wines.values
X = array[:,1:]
Y = array[:,0]  #选取class为目标变量
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2 #卡方检验
test = SelectKBest(score_func=chi2, k=2) #设置卡方检验，选择最佳特征
fit = test.fit(X, Y)
print(fit.scores_)
l = list(fit.scores_)
maxindex=[]
for i in range(2):
    maxindex.append(l.index(max(l)))
    l.remove(l[l.index(max(l))])
print("自动寻找出最佳特征为（无需人工筛选）：")
for i in maxindex:
    print(names[i + 1],end='')
print()
# fit.scores_.delete(np.argmax(fit.scores_))
# np.delete
# print(fit.index.name)
# features = fit.transform(X)
# print(features[0:5,:])


#绘图
color_intensity = df_wines['Color intensity']
proline = df_wines['Proline']
flavanoids = df_wines['Flavanoids']
wine_class = df_wines['class']


df_1_wine = df_wines[df_wines['class'] == 1]
df_2_wine = df_wines[df_wines['class'] == 2]
df_3_wine = df_wines[df_wines['class'] == 3]

bx = df_1_wine.plot.scatter(x='Color intensity', y='Proline', marker='*', color='plum', label='class_1')
df_2_wine.plot.scatter(x='Color intensity', y='Proline',  marker='x', color='lightskyblue', label='class_2', ax=bx)
df_3_wine.plot.scatter(x='Color intensity', y='Proline', marker='^', color='orange', label='class_3', ax=bx)
plt.title("两个个最相关特征影响" ,fontproperties="SimHei", fontsize=18)

plt.show()

#三维图
fig = plt.figure()
ax = Axes3D(fig)

color_intensity = pd.DataFrame(df_1_wine, columns = ['Color intensity'])
proline = pd.DataFrame(df_1_wine, columns = ['Proline'])
flavanoids = pd.DataFrame(df_1_wine, columns = ['Flavanoids'])
ax.scatter(color_intensity,proline,flavanoids,marker='*', color='plum', label = 'class_1')

color_intensity = pd.DataFrame(df_2_wine, columns = ['Color intensity'])
proline = pd.DataFrame(df_2_wine, columns = ['Proline'])
flavanoids = pd.DataFrame(df_2_wine, columns = ['Flavanoids'])
ax.scatter(color_intensity,proline,flavanoids,marker='x', color='lightskyblue', label = 'class_2')

color_intensity = pd.DataFrame(df_3_wine, columns = ['Color intensity'])
proline = pd.DataFrame(df_3_wine, columns = ['Proline'])
flavanoids = pd.DataFrame(df_3_wine, columns = ['Flavanoids'])
ax.scatter(color_intensity,proline,flavanoids,marker='^', color='orange', label = 'class_3')

plt.title("三个最相关特征影响" ,fontproperties="SimHei", fontsize=18)
ax.set_xlabel('Color intensity')
ax.set_ylabel('Proline')
ax.set_zlabel('Flavanoids')
ax.view_init(elev=10,azim=235)

plt.show()