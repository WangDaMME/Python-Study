import socketserver  # 多并发

class MyTCPHandle(socketserver.BaseRequestHandler):
    """
    The request handler class for our sever.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the client.
    """
    def handle(self):
        while True:
            try: # handle 来处理所有与客户端的交互， 不写循环 就是交互一次
                #self.request is the TCP socket connected to the client
                self.data=self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                '''
                if not self.data:  #收到data 为空,客户端为空
                    print("Client has lost...")
                    break            
                '''
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("err is :",e)
                break

if __name__ =="__main__":   # 只有被当做脚本才能执行，被import其他脚本不会被执行
    HOST, PORT = 'localhost', 9999

    #Create the server, binding to localhost on port 9999
    #server=socketserver.TCPServer((HOST,PORT),MyTCPHandle)
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandle)  # 多线程
    #socketserver.ForkingTCPServer() # 多进程
    # Activate the server, this will keep running until you interrupt the program with Ctrl-C
    server.serve_forever()
