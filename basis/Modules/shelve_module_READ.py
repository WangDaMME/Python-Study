import shelve

d=shelve.open("shelve_test")
#print(d.items())   #通过get读  #items都能显示
print(d.get("info"))
print(d.get("test"))

print("date",d.get("date"))
