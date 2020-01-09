import socket
import os
import hashlib


server=socket.socket()
server.bind(('localhost',8888))
server.listen()

while True:
    conn,addr= server.accept()
    print("new conn: ",addr)
    while True:
        print("waiting for the new command...")
        data=conn.recv(1024)
        if not data:
            print("Client has lost...")
            break;  #再接个电话
        cmd,filename = data.decode('utf-8').split()  # assume写死了的形式 “get filename"  # byte解码
        print(filename)
        if os.path.isfile(filename):                # 如果是个文件
            f=open(filename,'rb')     # 以byte二进制方式打开， 方便发送
            md=hashlib.md5()           # 安全加密
            file_size=os.stat(filename).st_size  # 发送文件大小 st_size
            conn.send(str(file_size).encode('utf-8'))           # 二进制字符串
            ack_client=conn.recv(1024)   # wait for ack 等待确认防止年报
            print('The client is acknowledged--->',ack_client.decode('utf-8'))
            for line in f:           # 迭代器发送
                md.update(line)      # md5 一行一行 转义
                conn.send(line)
            print("file md5 value is: ", md.hexdigest())
            f.close()
            conn.send(md.hexdigest().encode())  # 也可能在最后一行粘包 sticking

server.close()