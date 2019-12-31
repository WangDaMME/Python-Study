
class Animal(object):
    def __init__(self,name):
        self.name=name

    @staticmethod
    def animal_talk(obj):   # staticmethod makes function isolated from class
        obj.talk()

class Cat(Animal):
    def talk(self):
        print('Meow!')


class Dog(Animal):
    def talk(self):
        print('Bark Bark!')

d=Dog("Wangcai")
c=Cat("Tom")
Animal.animal_talk(d)
Animal.animal_talk(c)