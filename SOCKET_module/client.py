import socket

client=socket.socket()  # 声明socket类型，同时生成一个socket连接对象
client.connect(('localhost',9998))  #需要 ip地址 和端口port --以元组方式 (ip,port)
while True:
    msg = input(">>: ").strip()   #用户输入
    if len(msg)==0: continue     # 用户什么也没输入 空格... 会使 server占线 电话不会被挂断
    client.send(msg.encode("utf-8"))  # 转成二进制
    data = client.recv(1024)  # buffer:1024-- 1kb字节
    print('Clinet Received: ',data.decode("utf-8"))
#client.send(b"Hello World")
#client.send("哆啦a梦".encode("utf-8"))             # 穿中文

#data=client.recv(1024)  # buffer:1024-- 1kb字节
#print('client received:',data.decode("utf-8"))
client.close()