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

