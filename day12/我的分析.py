# 作者 ljc csv 文件读取
import numpy as np
# -*- coding: utf-8 -*-
# 利用Numpy进行分析
# 文件，名称 分割符号 下标为6，7的数据 ，分成两个数储存
c, v = np.loadtxt("data.csv", delimiter=",", usecols=(6, 7), unpack=True)
# print(c)
# print(v)
# 计算成交量的加权平均价格
vwap = np.average(c, weights=v)
# print(vwap)
# 计算算数平均价格
mean = np.mean(c)
# print(mean)
t = np.arange(len(c))
twap = np.average(c, weights=t)
# print(twap)
# 寻找最大值与最小值
h, l = np.loadtxt("data.csv", delimiter=",", usecols=(4, 5), unpack=True)
print(np.max(h))
print(np.min(l))
print((np.max(h) + np.min(l)) / 2)
print(np.ptp(h))
print(np.ptp(l))
# 统计分析
c = np.loadtxt("data.csv", delimiter=",", usecols=(6,), unpack=True)
print(np.median(c))
# print(np.sort(c))
v = np.var(c)
print(v)
# 股票收益率
c = np.loadtxt("data.csv", delimiter=",", usecols=(6,), unpack=True)
res = np.diff(c) / c[:-1]

print(np.std(res))
log = np.diff(np.log(c))
print(log)
pos = np.where(res > 0)
print(pos)
auu = np.std(log) / np.mean(log)
print(auu / np.sqrt(1. / 252.))
print(auu * np.sqrt(1. / 12.))
# 日期分析
from datetime import datetime


def datestr2num(s):
   return datetime.strptime(s, "%d-%m-%Y").date().weekday()

dates, close=np.loadtxt('data.csv', delimiter=',', usecols=(1,6),
                         converters={"1": datestr2num}, unpack=True)
print(dates)
