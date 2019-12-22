f_file=open("yesterday.txt",'r',encoding='utf-8')

# read 5 lines
'''
for i in range(5):
    print(f_file.readline())
    
'''
'''
for line in f_file.readlines():  # file.readline turns to be a list
    print(line.strip())          # strip the "\n"
'''

'''
# PLEASE FORGET READLINES
# Low quality - need more space
# !!!f.readlines only fit for small-size files 

# Print on the 10th line
for index, line in enumerate(f_file.readlines()):   #f_file.readlines() is a LIST
    if index==9:
        print("----- This is a Cut-off Line ----")
        continue     # skip the 10th line
    print(line.strip())
# low quality
'''


# high - quality
#iterator
'''
count=0
for line in f_file:
    if count==9:
        print("----- This is a Cut-off Line ----")
        count+=1
        continue
    count+=1
    print(line)

'''

'''
# Control with the handle  -- Tell & Seek
print(f_file.tell())   # start @ 0
f_file.readlines()
print(f_file.tell())   # end @
f_file.seek(0)         # set position
print(f_file.tell())   # end @
f_file.seek(10)         # set position
print(f_file.readline())

# Other function
print(f_file.encoding)  # encoding
print(f_file.isatty())
print(f_file.writable())
print(f_file.fileno())


f_file.close()

'''


# flush
import sys, time
for i in range(20):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)

