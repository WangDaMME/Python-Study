'''
# -*- coding:utf-8 -*-

name="wangda"
name2=name
name="kobe b"
print(name, "  +  ",name2)

# Inputm 
username=input("pls user name")
#print(username)

# Print
# 1. +
animal="dog"
age=4
info="Animal type is "+animal+"Old: "+str(age) #convert
print(info)

print("Animal is %s and Age is %d"%(animal,age))


# format
#1
name=input("name:")
age=input("age:")
job=input("job:")
info_a='''name: {Name}, age: {Age}, job: {Job}'''.format(Name=name,Age=age,Job=job)
print(info_a)


info_b='''name: {0}, age: {1}, job: {1}'''.format(name,age,job)
print("Info_b is",info_b)

import getpass

pswd=getpass.getpass("Password is :  ")

print(pswd)

'''
