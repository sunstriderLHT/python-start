# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#继承
#子类的方法__init__需要父类施以援手
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
class ElectricCar(Car):
    def __init__(self,make,model,year):
        #初始化父类属性，使用super继承
        super().__init__(make,model,year)
        
        #初始化电动汽车特有属性
        self.battery_size = 70
        
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kwh battery.")
        
        
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#重写父类方法
#可在子类中定义并重写一个与需要重写的父类方法
#在调用时python将忽略Car类的同名方法，转而运行子类的方法

#将实例用作属性
#将与电瓶有关的属性和方法提取出来放到名为Battery的类中
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kwh battery.")
    def get_range(self):
        if self.battery_size ==70:
            range1 = 240
        elif self.battery_size ==85:
            range1 = 270
        message = "This car can go approximately "+str(range1)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size !=85:
            self.battery_size =85
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()        
#9-6
class Restaurant():
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine = cuisine
    def descriptive_restaurant(self):
        print(self.name+" is a "+self.cuisine+ " restaurant.")
class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine):
        super().__init__(name,cuisine)
        self.flavors=['strawberry','apple','banana','pineapple']
    def show_flavors(self):
        print(self.flavors)
dairyQueen = IceCreamStand('dairyQueen','icecream')
dairyQueen.show_flavors()

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
