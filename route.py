# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:32:15 2021

@author: 朱洋
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:17:09 2021

@author: 朱洋
"""
import numpy as np
import pandas as pd
from numpy import array
from folium import plugins
import folium
import os
import tkinter as tk
import webbrowser as wb



network0 = pd.read_csv('最终数据.csv',index_col=0)
network0 = np.array(network0)
network1 = network0.tolist()

o1= input("输入起点：")

e=4 #任意数

def Dijkstra(network, s, d):  # 迪杰斯特拉算法算s-d的最短路径，并返回该路径和值
    # print("Start Dijstra Path……")
    path = []  # 用来存储s-d的最短路径1
    n = len(network)  # 邻接矩阵维度，即节点个数
    fmax = float('inf')
    w = [[0 for _ in range(n)] for j in range(n)]  # 邻接矩阵转化成维度矩阵，即0→max

    book = [0 for _ in range(n)]  # 是否已经是最小的标记列表
    dis = [fmax for i in range(n)]  # s到其他节点的最小距离
    book[s - 1] = 1  # 节点编号从1开始，列表序号从0开始
    midpath = [-1 for i in range(n)]  # 上一跳列表
    for i in range(n):
      for j in range(n):
        if network[i][j] != 0:
          w[i][j] = network[i][j]  # 0→max
        else:
          w[i][j] = fmax
        if i == s - 1 and network[i][j] != 0:  # 直连的节点最小距离就是network[i][j]
          dis[j] = network[i][j]
    for i in range(n - 1):  # n-1次遍历，除了s节点
      min = fmax
      for j in range(n):
        if book[j] == 0 and dis[j] < min:  # 如果未遍历且距离最小
          min = dis[j]
          u = j
      book[u] = 1
      for v in range(n):  # u直连的节点遍历一遍
        if dis[v] > dis[u] + w[u][v]:
          dis[v] = dis[u] + w[u][v]
          midpath[v] = u + 1  # 上一跳更新
    j = d - 1  # j是序号
    path.append(d)  # 因为存储的是上一跳，所以先加入目的节点d，最后倒置
    while (midpath[j] != -1):
      path.append(midpath[j])
      j = midpath[j] - 1
    path.append(s)
    path.reverse()  # 倒置列表
    return(path,dis)

#====================================================================================================================第一个出发点
result = Dijkstra(network1, int(o1), int(e))  
result1=list(result)
path=result1[0]
dis=result1[1]
ranking=np.argsort(dis)
rank1 = [x + 1 for x in ranking] 
rank=list(rank1)
finalrank=['' if i ==int(o1) else i for i in rank]

s1=(str(35))#此处修改终点
q1=rank.index(int(s1))

list1=[q1]
list2=[s1]
final=[x for _,x in sorted(zip(list1,list2))]
A=final[0]

Aresult = Dijkstra(network1, int(o1), int(A))  
Aresult1=list(Aresult)
Apath=Aresult1[0]
Adis=Aresult1[1]
Adistance = Adis[int(A)-1]
# print(Adistance)
print(o1,"逃生路径为:",Apath,Adistance)

