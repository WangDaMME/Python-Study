import re

res=re.match("^Wang\d+","Wang123Daa432DAAAA678")  #match from the **Beginning"  \d one number  \d+ : several numbers
print(res.group())
res=re.match(".+","Wang123Daa432DAAAA678")  #one character .+ many characters
print(res)

res=re.search("Daa.+AAA","Wang123Daa432DAAAA678")  # from str ... end with s
print(res.group())

res=re.search("D[a-z]+a","Wang123Daa432DssAAAA678")    # Daa number are excluded 不带数字的取法
print(res.group())
res=re.search("D[a-z]+A","Wang123Daa432DssAAAA678")    # Dss 前面的D不符合-- 不带数字的取法
print(res.group())

'''
res=re.search("W[a-zA-Z]+D","Wang123Daa432DssA678")    # Dss 前面的D不符合
print(res.group())
'''

res=re.search("D.+Daa","Wang123DaaDaa432DssAAAA678")  # 到Daa 结尾，.+
print(res.group())
res=re.search("W[a-z]+t","WangtWangtDaaDaa432DssAAAA678")  # 只会返回第一个
print(res.group())

res=re.findall("ab+","ab+cd+abb+bba")  # 所有 +号前 ab字符
print(res)

res=re.findall("ab*","cabb3abcbbac")  # 所有 +号前 ab字符
print(res)

#####?###
res=re.search("aa?","alex")  # 第一个a要有，第二个a可有 --结果a
print(res.group())

#
'''
res=re.search("aaa?","alex")  # 第一个aa要有，第二个a可有 --结果 None
print(res.group())
'''

# {m} {n,m}
res=re.search("[0-9]{3}","alss1ex2sss345sss")
print(res.group())
res=re.findall("ab{1,3}","abb abc abbcbbb")
print(res)

res=re.search("(abc){2}a(123|456)c", "abcabca456c").group()
print(res)

# Group '(?P<name>...)'
res=re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<Birthday>[0-9]{4})","371481199306143242").groupdict("city")
print(res)

res2=re.search("(?P<id>[0-9]+)","abcd12345@!#43243!@adsa")  # 想匹配数字 + 所有的数字
print(res2.groupdict())# 返回字典形式
res2=re.search("(?P<id>[0-9]{3})","abcd12345@!#43243!@adsa")  # 想匹配3位数字 + 所有的数字
print(res2.groupdict())# 返回字典形式

res3=re.search("(?P<id>[0-9]{3})(?P<name>[a-zA-Z]+)","abcd12345DaSdsA@!#43243!@adsa")  # 想匹配3位数字 + 所有的数字
print(res3.groupdict())# 按顺序的。
print(res3["id"])

# Split 分隔
res=re.split("[0-9]","abc12cd3fg5h4j6o") #返回列表
print(res)  # 1和 2没有分隔

res=re.split("[0-9]+","abc12cd3fg5h4j6o") #返回列表
print(res)  # 1和 2没有分隔

# Sub 替换
res=re.sub("[0-9]+","*","ab12ds45djk784ds231")
print(res)  #str 类型
#只换前两个 count=2
res=re.sub("[0-9]+","*","ab12ds45djk784ds231",count=2)
print(res)  #str 类型

# BackSlash