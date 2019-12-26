import configparser

config=configparser.ConfigParser() # object
print(config.sections())
config.read("example.ini",encoding='utf-8')
print(config.sections())
print(config.defaults()) # print Defaults Ordered dict 有序字典
print('bitbucket.org' in config)  # True
print('www.google.com' in config) # False
#print(config['bitbucket.org']['user'])  # index

'''
# Remove !!need write again
sec=config.remove_section("bitbucket.org")
config.write(open('example.ini','w'))   #bitbucket section is removed -- override files

'''


#Add section
sec2=config.add_section("www.google.com")
config.write(open('example.ini','w'))   #bitbucket section is removed
