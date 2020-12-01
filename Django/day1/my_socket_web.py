import socket

## 相当于 server 端

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # 实例  AF_INET: 基于ipv4,  SOCK_STREAM: 基于tcp_ip
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    sock.bind(('localhost',8000))                                # 监听 本机8000端口
    sock.listen(5)                                                # 最多允许 5 个链接排队

    #死循环 等着别人来连
    while True:
        #1.等待浏览器访问,   当浏览器 来了请求， accept 接收请求
        conn, addr = sock.accept()   # conn 根据这个请求生成实例对象
        #2. 接收 浏览器 发来的请求内容
        data = conn.recv(1024)    # 收1024个字符
        print(data)

        #3.给浏览器返回内容
        conn.send(b"HTTP/1.1 200 OK \r\n Content-Type:text/html; charset=utf-8\r\n\r\n")  # 通过 conn 这个对象 给浏览器返回内容  response_head
        conn.send("<h1 style='color:blue'>You are beautiful!</h1>".encode("utf-8"))

        # 4. 关闭和浏览器创建的socket链接
        conn.close()

main()

if __name__ == "main":
    main()
