
# open file
#open("yesterday.txt")
#data=open("yesterday.txt",encoding="utf-8").read() # default: charmap Need to tell to use UTF-8
#print(data)
f_file=open("yesterday.txt",'r',encoding='utf-8')
data=f_file.read()
'''
data2=f_file.read()
print(data)
print("----Data2---- The file point should be @ the end %s Nothing shows" %data2)
'''


'''
# write
f_file2=open("yesterday2.txt",'w',encoding='utf-8')
f_file2.write("I just wanna Rolly Rolly Rolly with a dab of ranch\n")
f_file2.write("I already got some designer to hold up my pants\n")

f_file2.close()
#a: append
f_file3=open("yesterday2.txt",'a',encoding='utf-8')
f_file3.write("I just want some ice on my wrist so I look better when I dance\n")
f_file3.write("Have you lookin' at it, put you in a trance…\n")
#data3=f_file3.read()
#print('data3---',data3)
'''

# read 5 lines
for i in range(5):
    print(f_file.readline())

f_file.close()
