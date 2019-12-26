import os
print(os.getcwd())  # 获取当前工作目录
#print(os.chdir("C:\Users\wangd\PycharmProjects\Python"))
#C:\\Users\\wangd\\PycharmProjects\\Python\\
# 两个斜杠\\ 第一个代表 转义，
# or 前面加个 r“C:\Users\wangd\PycharmProjects\Python“
'''
os.curdir # 返回当前目录 '.'
os.pardir # 返回当前目录的父亲目录  ‘..’
os.makedirs() # 生成多层递归目录 -- ie. 即使每一级目录不存在 r"C:\a\b\c\d"也会 逐级创建出来
os.removedirs() # r"C:\a\b\c\d" 逐级删除目录，直到有一个不是空的，C盘下 有东西，C盘就不清空
os.mkdir()  # 生成单级目录，相当于shell 中的mkdir dirname
os.rmdir()  # 删除单级目录
os.remove() # 单删一个文件
os.rename("oldname","newname") #改名
os.stat()  # 获取文件/目录信息
os.sep     #输出操作系统特定的路径分隔符，win下为\\, linux 下为/
os.linesep #输出当前平台使用的 行终止符， win 下为“ \t\b”, linux下为 "\n"
os.pathsep #输出用于分隔文件路径的字符串  win 下 每个path路径分隔 “；”分好、号
os.environ  #查看当前系统环境变量

os.system("bash command") # 运行shell 命令，直接显示
eg
os.system('dir') #查看当前目录下内容
'''
print(os.listdir('.'))  #列出指定目录下所有文件和子目录，包括隐藏hidden文件，并以列表方式 打印
print(os.environ)  # 字典格式
print(os.name)  # os.name 当前操作系统名 ie windows
os.system('ipconfig /all') #windows ip配置
#os.path
'''
os.path.abspath(path)   #返回规范化的绝对路径
os.path.split(path)     #将path分隔成 （目录，文件名） （tuple 二元组）返回
os.path.dirname(path)   #获取目录名, 就是返回os.path.split的第一个元素
os.path.basename(path)  #返回path最后面 的文件名。如果path以/或\结尾，会返回空值，ie.os.path.split的第2个元素
os.path.exists(path)    #path 是否存在 返回true，否则false
os.path.isabs(path)     #是否是绝对路径，   绝对路径：从某个根路径开始, win 可以有多个根 C D E盘... 
                        #                 linux： 以"/"开头,ie.从root开始
                        # 相对路径： 没有根root开头的
os.path.isfile()        # 是否存在 该文件
os.path.isdir()         # 是否是一个存在的目录
os.path.join(path1[,path2[,...]])  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
                                   #os.path.join(r'C:',r'\a.txt')
os.path.getatime(path)  # 获取 path所指向文件或者目录 最后的 【存取】 时间 in Second [s]
os.path.getmtime(path)  # 获取 path所指向文件或者目录 最后的 【修改】 时间 in Second [s]

'''
