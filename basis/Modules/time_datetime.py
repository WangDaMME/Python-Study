import time

print(time.localtime()) #y,m,d,h,m,s, weekday,yearday,dst: summertime 本地时间
# 获取属性 attribute
x=time.localtime()
print("Day and Year",x.tm_mday,x.tm_year)
print(time.mktime(x)) # 传入 sturct_time 元组 返回  多少s
print(time.altzone/3600) #返回与utc相差时间 s
print(time.asctime()) # 返回时间格式Tue Dec 4 21:15:15 2019
print(time.timezone/3600) # 返回时区
print(time.time())   # 获取时间戳 timestamp
#time.sleep(3)        # 睡几s
print(time.gmtime(time.time()))  # 返回utc时间的 struct_time元组
str=time.strftime("%Y-%m-%d %H:!@#!@%M:%S")  # string format time 用% 打印出 字符串 格式化输出
print(type(str))
print(str)

a=time.strptime('2019-12-24 21:!@#!@36:17',"%Y-%m-%d %H:!@#!@%M:%S")
print(a)   # strptime（str_format格式化字符串，format） --> 返回 time_struct

print(time.ctime())   # 把时间戳timestamp 显示成 这种格式

print("===========Datetime Module=======")
# datetime 时间的操作 加减
import datetime
print(datetime.datetime.now())   # 当前时间
print(datetime.datetime.now()+datetime.timedelta(-3))  # 默认 3天 days
print(datetime.datetime.now()+datetime.timedelta(hours=3))  # 默认 3天 days
print(datetime.datetime.now()+datetime.timedelta(seconds=30))
print(datetime.datetime.now()+datetime.timedelta(hours=30))