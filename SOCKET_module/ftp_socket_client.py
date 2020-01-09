import socket
import hashlib
client=socket.socket()
client.connect(('localhost',8888))

while True:
    cmd=input(":>> ").strip()
    if len(cmd)==0: continue
    if cmd.startswith("get"):
        client.send(cmd.encode('utf-8'))
        file_size=int(client.recv(1024).decode('utf-8'))
        client.send("The client is ready, sticking-proof...".encode('utf-8'))
        recv_size=0
        # 打开一个新文档存储
        file_new =open(cmd.split()[1]+"_new.txt",'wb')  # 起一个新名 以wb形式写
        md=hashlib.md5()

        while recv_size<file_size:
            # 防最后一次发md5粘包，
            if file_size-recv_size >1024:  # 要收不止一次
                size=1024
            else: # 最后一次剩多少，收多少
                size=file_size-recv_size
                #print("last turn receives: ",size)
            data=client.recv(size)  # 最大一次接收1024
            recv_size+=len(data)
            md.update(data)
            file_new.write(data)

            #打印进度
            #print("%d is out of %d"%(recv_size,file_size))  # 打印让程序变慢
        else:
            new_file_md5=md.hexdigest()
            print("All file is copied completely",file_size)
            file_new.close()
        server_file_md5=client.recv(1024)
        print("server file md5: ",server_file_md5)
        print("client file md5: ",new_file_md5)
    else:
        print('Wrong Command, start with "Get"!')

client.close()