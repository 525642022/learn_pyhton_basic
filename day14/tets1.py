# 作者 ljc
import numpy as np
import os
from scipy.interpolate import lagrange
from pandas import Series, DataFrame
import pandas as pd
import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt

np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))
##确实值处理——————拉格朗日算法
inputfile = "data/catering_sale.xls"
outputfile = "data/sale.xls"

data = pd.read_excel(inputfile)
# print(data)
row_index = (data[u"销量"] < 400) | (data[u"销量"] > 5000)
data.loc[row_index, u"销量"] = None


# 自定义向量与数值函数
# s为列向量 n 为被差值的位置，k 为取前后数值个数，默认为5
def ployinterp_column(s, n, k=5):
    y = s.reindex([list(range(n - k, n)) + list(range(n + 1, n + 1 + k))])  # 取数
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)  # 插值并返回结果


for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            # print(ployinterp_column(data[i], j))
            data.loc[j, i] = ployinterp_column(data[i], j)
data.to_excel(outputfile)
# print(data)
# 关于异常值得处理
# 合并数据
# merge方法 根据一个或多个键将不同的dataFrame中进行合并
# Concat方法 沿一个轴将对多个对象堆叠起来
# 数据库风格的DataFrame的合并
# merge
# merge参数
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'],
                 'data2': range(3)})
print(df1)
print(df2)
# 合并data
df3 = pd.merge(df1, df2)
print(df3)
df4 = pd.merge(df1, df2, on="key")
print(df4)
# 2
df5 = DataFrame({"lkey": ['b', 'd', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df6 = DataFrame({'rkey': ['a', 'b', 'd'],
                 'data2': range(3)})

d7 = pd.merge(df5, df6,left_on='lkey',right_on='rkey')

d8=pd.merge(df1, df2, how='outer')
#表示现在进行外连接
print(d7)
print(d8)



#索引合并
left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],'value': range(6)})
right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
print(left1)
print(right1)

mypd=pd.merge(left1,right1,left_on='key',right_index=True)
print(mypd)


