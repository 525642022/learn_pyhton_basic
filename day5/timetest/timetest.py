# 作者 ljc
import time

# 从1970到现在的时间的秒数
print(time.time() / 3600 / 24 / 365)
# 格式化的时间字符串

#元组元素
print(time.localtime())
print(time.timezone/3600)
# time.sleep() 睡几秒
time.sleep(1)
# time.gmtime()  时间戳---->元组 转换成utc时间
print(time.gmtime())
# time.localtime() 时间戳---->元组 本地时间  默认为当前时间
mytime=time.localtime()
print(mytime.tm_year)
# time.mktime() 元组 --->时间戳
# time.strftime("%Y-%m-%d %H:%M:%S") 元组转格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S",mytime))
# time.strptime() 逆向转换 与strftime 格式化时间转元组
# time.ctime()
# print(time.ctime()) 时间戳转格式化字符串
# print(time.asctime())元组转格式化字符串
#--------------dataTime————————-------
import  datetime
print(datetime.datetime.now()+datetime.timedelta(3))