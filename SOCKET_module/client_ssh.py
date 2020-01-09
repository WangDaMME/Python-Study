import socket

client = socket.socket()
client.connect(('localhost',6666))
while True:
    msg=input(":>> ").strip()
    if len(msg)==0:   #不能发送 空数据 ，recv阻塞函数会卡
        continue
    client.send(msg.encode('utf-8'))  # 以二进制 形式发送

    cmd_res_size=int(client.recv(1024).decode('utf-8'))  # 收返回的大小二进制 str转成 int 证书
    print("the size is: ",cmd_res_size)
    client.send("Ready for receiving".encode('utf-8'))  # 防止粘包
    recv_size=0
    recv_data= b''
    # 大数据循环收
    while recv_size<cmd_res_size:
        data=client.recv(1024)   # 最大接收1024
        recv_size += len(data)   # 不是每次收1024 是最大，还有 发单个的情况
        recv_data+=data
    else:
        print("---All result is received---",recv_size)
        print(recv_data.decode('utf-8'))

client.close()