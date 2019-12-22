'''
import os

os.system("dir")
cmd_res=os.system("dir")
print("The Result of Sys cannot be saved: ----\n",cmd_res)
# Savable
cmd_res_saved=os.popen("dir").read()
print("---->",cmd_res_saved)
'''

a,b,c,d=1,3,5, 7
e = a if b>c else d
print(e)

print("String ---> Byte: Encode")
msg_en="Hello World!"
print(msg_en.encode(encoding="utf-8"))
msg_ch="我爱北京天门"
print(msg_ch.encode(encoding="utf-8"))

print("Byte ---> string: Decode")
print(msg_en.encode(encoding="utf-8").decode(encoding="utf-8"))
print(msg_ch.encode(encoding="utf-8").decode(encoding="utf-8"))


