from wsgiref.simple_server import make_server


# 当用户 在浏览器访问 http://127.0.0.1:8000 , 立即执行该函数 并将 函数的返回值返回给用户
def run_server(environment, start_response):
    """
    :param environment 浏览器 详细 数据, 请求相关内容 eg浏览器类型，版本，来源地址,url等
    :param start_response 响应的相关内容
    """

    print("hahaha")

    start_response("200 OK",  [('Content-Type', 'text/html;charset=utf-8')])   # 列表 [元组 ()]
    return [bytes('<h2>  good job wsgiref! </h2>',encoding='utf-8'),]  #bytes 类型



s= make_server('localhost',8000,run_server)  # 回调函数
s.serve_forever()   # 死循环