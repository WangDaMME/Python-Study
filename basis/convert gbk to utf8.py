#-*-coding:gbk -*-    # declare file coding �ļ�����
import sys
print(sys.getdefaultencoding())

str="���"  # python Ĭ��unicode
print(str.encode("gbk"))
print(str.encode("utf-8"))
print(str.encode("gb2312"))
