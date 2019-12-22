#-*-coding:gbk -*-    # declare file coding 文件编码
import sys
print(sys.getdefaultencoding())

str="你好"  # python 默认unicode
print(str.encode("gbk"))
print(str.encode("utf-8"))
print(str.encode("gb2312"))
