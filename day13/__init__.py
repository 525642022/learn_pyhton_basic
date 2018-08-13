# # 作者 ljc Pandas 练习
# # 数据结构 series  数组 与 标签
# # 可以通过标签选取数组
# # 定长有序数组
import pandas as pd
import numpy as np
import sys

from pandas import Series, DataFrame

#
# obj = Series([4, 7, -5, -3])
# print(obj)
# print(obj.values)
# print(obj.index)
# obj2 = Series([1, 3, -5, 7], index=["d", "b", "a", "c"])
# print(obj2)
# print(obj2.index)
# print(obj2[obj2 > 0])
# print(obj2 * 2)
# print(np.exp(obj2))
# print("b" in obj2)
# print("m" in obj2)
# sdata = {"name": "ljc", "age": 20, "adress": "bj"}
# obj3 = Series(sdata)
# print(obj3)
# print(pd.isnull(obj3))
# print(pd.notnull(obj3))
# # 如果都同时存在 则进行运算，如果不同时存在 则会NaN变为确实
#
# print(obj3 + obj2)
# obj3.name = "lll"
# obj3.address = "ssss"
# print(obj3)
# # dataframe 表格行数据结构
# # 行索引、列索引
# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
#         'year': [2000, 2001, 2002, 2001, 2002],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# frame = DataFrame(data)
#
# print(frame)
# frame1 = DataFrame(data, columns=["year", "state", "pop"])
# print(frame1)
#
# frame2 = DataFrame(data, columns=["year", "state", "pop", "hello"], index=["one", "two", "three", "four", "five"])
# print(frame2)
# print(frame2.columns)
# print(frame2["state"])
# print(frame2.year)
# print(frame2.ix["three"])
# frame2["debt"] = np.arange(5.)
# print(frame2)
# # 索引对象
# obj = Series(range(3), index=["a", "b", "c"])
# index = obj.index
# print(index)
# # 索引对象是不能修改的
#
# # Pandas提供一些一些用于将表格型数据读取为DataFrame对象的函数
# df = pd.read_csv("data/ex1.csv")
# print(df)
# df1 = pd.read_table("data/ex1.csv", sep=",")
# print("df1", df1)
# df = pd.read_csv("data/ex1.csv", header=None)
# print(df)
#
# df = pd.read_csv("data/ex1.csv", names=["a", "b", "c", "d", "message"])
# print(df)
# names = ["a", "b", "c", "d", "message"]
#
# df = pd.read_csv("data/ex1.csv", names=names, index_col="message")
# print(df)
# df = pd.read_csv("data/csv_mindex.csv", index_col=["key1", "key2"])
# print(df)
# res = pd.read_table("data/ex3.txt", sep="\s+")
# print(res)
# df = pd.read_csv("data/ex5.csv", na_values=["NULL"])
# print(df)
#
# # 逐行读取文件
# res = pd.read_csv("data/ex6.csv")
# # print(res)
# chunker = pd.read_csv("data/ex6.csv", chunksize=1000)
# print(res)
# tot = Series([])
# for piece in chunker:
#     tot = tot.add(piece['key'].value_counts(), fill_value=0)
#
# # tot = tot.order(ascending=False)
#
# print(tot[:10])
# # 文件写入
# data = pd.read_csv("data/ex5.csv")
# print(data)
# data.to_csv("out.csv")
#
# data.to_csv(sys.stdout, sep="|", na_rep="NULL", index=False, header=False)
#
# data.to_csv(sys.stdout, index=False, columns=["a", "b", "c"])
#
# # 手动处理分隔符
# import csv
#
# f = open("data/ex7.csv")
# reader = csv.reader(f)
# for line in reader:
#     print(line)
#
# lines = list(csv.reader(open('data/ex7.csv')))
# header, values = lines[0], lines[1:]
# print("___", header)
# print("----", values)
# for h, v in zip(header, zip(*values)):
#     print(h, v)
# data_dict = {h: v for h, v in zip(header, zip(*values))}
# print(data_dict)
#
# import xlrd, xlwt
#
# path = "data/"
# wb = xlwt.Workbook()
# print(wb)
# wb.add_sheet("first", cell_overwrite_ok=True)
# print(wb.get_active_sheet())
# ws1 = wb.get_sheet(0)
# print(ws1)
# ws2 = wb.add_sheet("second_sheet")
# data = np.arange(1, 65).reshape(8, 8)
# print(data)
# ws1.write(0, 0, 1)
# for c in range(data.shape[0]):
#     for r in range(data.shape[1]):
#         print("--",c,r,data[c,r])
#         ws1.write(c,r, int(data[c,r]))
#         ws2.write(c, r, int(data[r, c]))
# wb.save(path + "work.xls")
# #从工作簿中读取
# book=xlrd.open_workbook(path+"work.xls")
# print(book)
# print(book.sheet_names())
# sheet1=book.sheet_by_name("first")
# sheet2=book.sheet_by_index(1)
# print(sheet1)
# print(sheet2.name)
# print(sheet1.ncols)
# print(sheet1.nrows)
# c1 = sheet1.cell(0,0)
# print(c1.ctype)
#
# print(sheet2.row(3))
#
#
# xls_file=pd.ExcelFile(path+"work.xls")
# table=xls_file.parse("first")
# print(table)

# json数据
obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
              {"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""
import json

res = json.loads(obj)
print(res)
asjosn = json.dumps(res)
print(asjosn)
sibling = DataFrame(res["siblings"], columns=["name", "age"])
print(sibling)
# 二进制格式
frame = pd.read_csv("data/ex1.csv")
print(frame)
frame.to_pickle("data/pickle")
pd.read_pickle("data/pickle")
import requests

url = 'https://api.github.com/repos/pydata/pandas/milestones/28/labels'
resq = requests.get(url)
print(resq)
data = json.loads(resq.text)
print(data)
issue = DataFrame(data)
print(issue)
print(issue.get("default"))

import sqlite3

query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
 c REAL,        d INTEGER
);"""
con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()

data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

con.executemany(stmt, data)
con.commit()
cursor = con.execute('SELECT * FROM test')
rows = cursor.fetchall()
print(rows)
datas = DataFrame(rows, columns=list(zip(*cursor.description))[0])
print(datas)
import  pandas.io.sql as sql
print(sql.read_sql('SELECT * FROM test',con))