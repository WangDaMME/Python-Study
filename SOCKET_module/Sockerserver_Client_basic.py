import socket

client=socket.socket()
client.connect(('localhost',9999))

while True:
    msg=input(":>> ").strip()
    if len(msg)==0: continue
    client.send(msg.encode())
    data=client.recv(1024)
    print("The client received data", data.decode('utf-8'))


client.close()
