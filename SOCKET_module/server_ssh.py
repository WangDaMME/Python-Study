import socket
import os

server=socket.socket()
server.bind(('localhost',6666))
server.listen()
while True:
    conn, addr = server.accept()
    print("New conn:", addr)
    while True:
        data=conn.recv(1024)   # 【最大】接收1024， 一次发过来10个他也收
        if not data:           # recv 为阻塞函数， 如果data 为空直接跳出另接一客
            print('The client is disconnected...')
            break
        print("The server received: ", data)
        cmd_res= os.popen(data.decode('utf-8')).read()      # popen需要传 字符串， 不是二进制 decode成二进制
        print("before send..,",len(cmd_res))
        if len(cmd_res)==0:
           cmd_res='This cmd has no output, my boy! '

        # ipconfig 这种超过1024的信息 并不能一次传输
        # 1. 先告诉client的大小
        #conn.send(str(len(cmd_res)).encode('utf-8'))  # send 只能发字符串，不能发整数，以二进制方式

        '''----- 有encode 很关键 [因为系统如果有一些带中文的指令 返回结果为多]    a="你"
        print(len(a))                       --- and:1
        print("By Byte", len(a.encode()))   --- ans: 3'''
        conn.send(str(len(cmd_res.encode('utf-8'))).encode('utf-8'))  # send 只能发字符串，不能发整数，以二进制方式
        # Sticking 粘包  - 当两个send操作同时出现，buffer有时候会把这种强制操作 合并为一次
        # time.sleep(0.5)
        client_ack=conn.recv(1024)     # wait client to confirm
        print("acknowledged by the client",client_ack)
        conn.send(cmd_res.encode('utf-8'))  # 以二进制方式传输
        print("send done")

server.close()