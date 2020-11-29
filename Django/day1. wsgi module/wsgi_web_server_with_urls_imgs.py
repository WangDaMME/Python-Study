
# 1. 路由分发器，  负责把url 匹配到对应的函数
# 2. 开发好 对应的 业务函数
# 3. 一个请求来了 之后， 先走路由分发器，
#     3.1 如果找到对应的func 就执行
#     3.2 没有找到 返回404

from wsgiref.simple_server import make_server

import re  # 正则表达式
import os # 打开文件

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#routing 路由分发器
def url_dispatcher():
    # hardcoded
    urls = {
        '/mercedes': mercedes,   #不加括号 是定义不是执行
        '/maserati': maserati,
    }

    return urls  # 返回字典

def mercedes(environment, start_response):
    print('mercedes web page ')
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])  # 列表 [元组 ()]

    data = """
        <h1> Welcome to Mercedes Shop </h1>
             <img src='/static/imgs/mercedes_img.jpg' />
        <p> Do you like it? please pay </p>
    """
    # static 只是前段路径的表示
    # return [bytes('<h2 style="color:blue">  BOOK web page ! </h2>', encoding='utf-8'), ]  # bytes 类型
    return [bytes(data, encoding="utf-8")]

def maserati(environment, start_response):
    print('maserati web page ')
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])  # 列表 [元组 ()]

    data = """
            <h1> Welcome to Maserati Shop </h1>
                <img src ='/static/imgs/maserati_img.jpg'/>
            <p> Do you like it? please pay </p>
        """
    #return [bytes('<h2 style="color:red">  CLOTH web page ! </h2>', encoding='utf-8'), ]  # bytes 类型
    return [bytes(data, encoding="utf-8")]

def image_handler(request_url):
    # param request_url : /static/imgs/maserati_img.jpg
    #print("BASE_DIR",BASE_DIR);

    img_path = re.sub('/static','/static_data', request_url)
    image_abs_path = "%s%s"%(BASE_DIR,img_path)
    print("image absolute path",image_abs_path)
    # 先判断文件 存不存在,再打开 否则出错
    print(os.path.isfile(img_path))

    if os.path.isfile(image_abs_path):
        print('file exists')
        f = open(image_abs_path,"rb")  # 二进制形打开
        data = f.read()
        return [data, 0]  # 加 状态码： 0代表没错， 1 代表有错

    #else
    return [None,1] #没有图片



def run_server(environment, start_response):

    print ("do work...")

    url_list = url_dispatcher()  # 拿到所有的url

    request_url = environment.get("PATH_INFO")
    #print('request url', request_url)

    # 判断在不在 字典里
    if request_url in url_list:
        result_data = url_list[request_url] (environment, start_response)  # 直接执行
        return result_data    # 真正返回给用户
    elif request_url.startswith("/static"):  #代表图片
        image_data, image_status = image_handler(request_url)  # 图片地址 传进来
        if image_status ==0: # 有内容
            start_response("200 OK", [('Content-Type', 'text/jpeg;charset=utf-8')]) #包装个 响应头 response head  返回的是jpeg
            return [image_data,]  # return 成列表的格式
    else:
        start_response("404 ", [('Content-Type', 'text/html;charset=utf-8')])
        return [bytes('<h2> 404 - Page Not Found ! </h2>', encoding='utf-8'), ]


s=make_server('localhost',8000,run_server)
s.serve_forever()