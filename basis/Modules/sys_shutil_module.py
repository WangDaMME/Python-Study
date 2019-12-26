#==================SYS==================#
import sys
'''
print(sys.argv)  #命令行参数路径，第一个元素是程序本身路径
sys.exit(n)      #退出程序，正常退出时exit(0)

'''
'''
print(sys.version)  # 获取python解释程序的版本信息
print(sys.path)   #返回 模块的搜索路径，初始化时，使用pythonpath环境变量的值
print(sys.platform) #返回 操作系统平台名称
sys.stdout.write('Hello world')  # 标准输出
val=sys.stdin.readline()[:-1]  #输入
print(val)

'''


#==================Shutil==================#
import shutil
'''
f1=open("notebook.txt",encoding="utf-8")
f2=open("notebook_copy.txt","w",encoding="utf-8")
shutil.copyfileobj(f1,f2)   # copyfileobj 需要事先打开2个文件
'''
shutil.copyfile("notebook_copy.txt","notebook_copyV2.txt") #不用事先打开文件，直接拷贝
#shutil.copymode(src,dst) #仅拷贝权限，内容、组。用户均不变
#shutil.copustat(src,dst) #拷贝状态的信息，包括：mode bits, atmie,mtime,flags
'''
shutil.copy(src,dst)  #拷贝 文件&权限
shutil.copy2(src,dst)  #拷贝 文件&状态信息

shutil.copytree("源目录"，"新目录") #拷贝目录
shutil.rmtree("新目录") #删除目录
shutil.move(src,dst)  #移动文件
'''
shutil.make_archive(base_name=,format,...) #tar 只能包，不压缩， zip又打包又压缩

import zipfile

z=zipfile.ZipFile(,'w') #默认是读, 'w'是压缩