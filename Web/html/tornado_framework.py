import tornado.ioloop
import tornado.web

# web framework and asynchronous library
# pip3 install tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(' Get_Method Connected !')
        u= self.get_argument('user')
        e=self.get_argument('email')
        p=self.get_argument('pwd')
        if u=='wangda' and e=='123@gmail.com' and p=='123':
            self.write('All info. are good !')
        else:
            self.write("!!!Get Out!!!")
    def post(self,*args, **kwargs):
        u=self.get_argument('user',None)
        e=self.get_argument('email',None)
        p=self.get_argument('pwd',None)

        print(u,e,p)
        self.write('Post_Method Connected')

application = tornado.web.Application([(r"/index",MainHandler),])

if __name__ == "__main__":
    print('it is listening...')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
