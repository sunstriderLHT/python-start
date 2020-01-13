class Dog():
#首字母大写的一般是类
    def __init__(self,name,age):
        #初始化属性name和age
        #当用Dog类创建新实例时，python都会自动运行__init__方法
        #__init__中有3个方法，形参self必不可少还必须位于其他形参之前
        #创建实例时，self会被自动传入，self 是指向实例本身的
        #每次我们根据Dog创建实例时，都只需要给name和age提供值
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        print(self.name.title()+" rolled over!")

my_dog=Dog('willie',6)
print(my_dog.name.title()+' is '+str(my_dog.age)+' years old')
my_dog.sit()
my_dog.roll_over()

print("\n")
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print("This restaurant is opening")
NBW = Restaurant('Niubingwei','BBQ')
NBW.describe_restaurant()

print("\n")
#汇总信息
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

#给属性指定默认值，在方法__init__()内指定初始值，就无需包含为它提供初始值的形参
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("this car has "+str(self.odometer_reading)+" miles on it.")
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#修改属性值
# 1.直接修改属性的值
my_new_car.odometer_reading=23
my_new_car.read_odometer()
# 2.通过方法修改属性的值
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("this car has "+str(self.odometer_reading)+" miles on it.")
    
    def update_odometer(self,meters):
        self.odometer_reading=meters
my_new_car=Car('audi','a4',2016)
my_new_car.update_odometer(23)
my_new_car.read_odometer()