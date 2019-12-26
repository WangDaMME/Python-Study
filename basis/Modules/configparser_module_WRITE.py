import configparser

config=configparser.ConfigParser()  # 生成类的 对象
#print(type(configparser.ConfigParser()))  # 类

# Key Value 形式 添加 节点
config["DEFAULT"] ={'ServerAliveInternal':45,
                    'Compression' : 'yes',
                    'CompressionLevel':9,

}

#2nd node
config['bitbucket.org']={}
config['bitbucket.org']['User']='hg'

#3rd node
config['topsecret.server.com']={}
topsecret=config['topsecret.server.com']
topsecret['Host Port']='50022'  # mutates the parser
topsecret['ForwardX11']='no'  # mutates the parser

config['DEFAULT']['ForwardX11']='yes'

with open('example.ini','w') as configfile:
    config.write(configfile)