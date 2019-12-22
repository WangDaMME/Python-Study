f_ori_read=open("yesterday.txt",'r',encoding='utf_8')
f_new_write=open("yesterday.bak",'w',encoding='utf_8')

for line in f_ori_read:
    if "wild pleasures lay in store for me" in line:
        #f_new_write.write("wild pleasures lay in store for Michael Da WANG!\n")
        #continue
        line=line.replace(line,"wild pleasures lay in store for Michael Da WANG!\n")
    f_new_write.write(line)

f_new_write.close()
f_ori_read.close()

'''

# shell sed
import sys
str_find = sys.argv[1]
str_replace = sys.argv[2]
for line in file:
    if str_find in line:
        line=line.replace(str_find,str_replace)
    file.write(line)
'''
