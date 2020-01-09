import socket
#import os

server=socket.socket()
server.bind(('localhost',9998))  # 绑定要监听的端口
server.listen(3)  # 开始监听 3个
print("Waiting for calls...")
while True:       # 每挂断一个 就能再接个电话
    conn, addr = server.accept()  # 等待别人打电话 监听到东西时，把con，address 谁打的电话返回
    # conn写在里面就会 重新 再接一个电话
    #conn 客户端连过来而在服务器端为其生成的一个连接实例
    print(conn, addr)
    count=0
    while True:

        data=conn.recv(1024)   # 收到的信息
        if not data:
            print("client has lost...")  #如果client断开
            break
        #res = os.popen(data).read()
        #conn.send(res)
        print("Server Received", data.decode("utf-8"))    # 中文转码
        conn.send(data.upper()) # 再给client 发一个信息
        count+=1
        if count>10: break

server.close()