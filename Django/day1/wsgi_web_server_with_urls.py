
# 1. 路由分发器，  负责把url 匹配到对应的函数
# 2. 开发好 对应的 业务函数
# 3. 一个请求来了 之后， 先走路由分发器，
#     3.1 如果找到对应的func 就执行
#     3.2 没有找到 返回404

from wsgiref.simple_server import make_server

#routing 路由分发器
def url_dispatcher():
    # hardcoded
    urls = {
        '/book': book,   #不加括号 是定义不是执行
        '/cloth': cloth,
    }

    return urls  # 返回字典

def book(environment, start_response):
    print('book web page ')
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])  # 列表 [元组 ()]
    return [bytes('<h2 style="color:blue">  BOOK web page ! </h2>', encoding='utf-8'), ]  # bytes 类型


def cloth(environment, start_response):
    print('cloth web page ')

    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])  # 列表 [元组 ()]
    return [bytes('<h2 style="color:red">  CLOTH web page ! </h2>', encoding='utf-8'), ]  # bytes 类型

def run_server(environment, start_response):

    print ("do work...")

    url_list = url_dispatcher()  # 拿到所有的url

    request_url = environment.get("PATH_INFO")
    print('request url', request_url)

    # 判断在不在 字典里
    if request_url in url_list:
        result_data = url_list[request_url] (environment, start_response)  # 直接执行
        return result_data    # 真正返回给用户
    else:
        start_response("404 ", [('Content-Type', 'text/html;charset=utf-8')])
        return [bytes('<h2> 404 - Page Not Found ! </h2>', encoding='utf-8'), ]


s=make_server('localhost',8000,run_server)
s.serve_forever()