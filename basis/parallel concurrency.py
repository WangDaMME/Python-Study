import time

def consumer(name):
    print("Consumer - %s is coming to eat cookie!"%name)
    while True:
        cookie =yield
        print("Consumer - {0} is done having cookie - {1}!".format(name,cookie))

'''
c=consumer("michael")
c.__next__()
c.__next__()
c.__next__()
c.send("chocholate")
c.send("chocholate")
c.__next__()
c.send("blueberry")
'''

def store(name):
    c1=consumer('A')
    c2=consumer('B')
    c1.__next__()
    c2.__next__()
    print("The store - %s is preparing the cookies"%name)
    for i in range(10):
        time.sleep(1)
        print("Done 2 cookies")
        c1.send(i)
        c2.send(i)

store("Reese")