import hashlib

m=hashlib.md5()  # 生成要加密对象 with md5 算法
# 传byte 二进制类型
m.update(b"Hello")
print(m.hexdigest())
m.update(b"It's me")
print(m.hexdigest())  # 是 之前的内容 hello 和 It's me一起的内容
#collison
m2=hashlib.md5()
m2.update(b"HelloIt's me")
print(m2.hexdigest())

#sha1
s1=hashlib.sha1()
s1.update(b"HelloIt's me")
print("sha1",s1.hexdigest())
print("10 dg",s1.digest())  # 10dc key

import hmac
h=hmac.new("天王盖地虎".encode(encoding="utf-8"),b"valuueeee")  # key/value only ascii
print('10dc',h.digest())
print('hex',h.digest())


