class Animal:
    name,age=0,0
    def sayHello(self):
        self.name='Animal'
        self.age=3
        print('hell！I am %s,I am %d yrear old'%(self.name,self.age))
class Dog(Animal):
    def sayHello(self):
        self.name='Snoopy dog'
        self.age=2
        print('wangwang~~hell！I am %s,I am %d yrear old'%(self.name,self.age))
class Cat(Animal):
    def sayHello(self):
        self.name='Coffee cat'
        self.age=3
        print('miaomiao~~hell！I am %s,I am %d yrear old'%(self.name,self.age))
my=Animal()
my.sayHello()
my=Dog()
my.sayHello()
my=Cat()
my.sayHello()