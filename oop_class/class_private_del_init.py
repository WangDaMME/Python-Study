class Role(object):
    # 构造
    nationality="Chinese"
    def __init__(self,name,job,weapon,money=2000):
        self.name=name
        self.job=job
        self.weapon=weapon
        self.__life_value=100  # private attrib
        self.__money=money

    def got_shot(self):
        self.__life_value-=20
        print("%s got shot"%self.name)
        self.show()

    def show(self):   #port to show private
        print("My life balance is : ",self.__life_value)

    def __AddMoney(self):
        self.__money+=10000

    def Gotothebank(self):
        self.__AddMoney()
        print("The current money is : ",self.__money)

    def __del__(self):  # no parameter
        print("____DEL____", self.name)


r1=Role("Mike","police","b46")
r1.got_shot()
r1.got_shot()
#print(r1.__life_value)
#r1.__AddMoney()
r1.Gotothebank()
r1.Gotothebank()
r1.Gotothebank()
del r1
r2=Role("Kris","terr","b11")  # 析构在最后释放
r2.got_shot()
r2.got_shot()
r3=Role("Xigou","police","b51")  # 析构在最后释放
r3.got_shot()
r3.got_shot()


