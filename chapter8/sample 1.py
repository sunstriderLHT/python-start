#函数
def favorite_book(title):
    print("One of my favorite book is "+title)
favorite_book('Alice in Wonderland')

#位置实参(基于实参顺序)
def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+ animal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster','harry')

#关键字参数(传递给函数的名称-值对，无需考虑函数调用中的实参顺序)
def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+ animal_type+"'s name is "+pet_name.title()+".")
describe_pet(pet_name='harry',animal_type='hamster')

#默认值(可给每个形参指定默认值，在调用函数中给形参提供了实参时，使用指定的实参值，否则使用形参的默认值)
#有默认值的参数要放在位置参数后面
def describe_pet(pet_name,animal_type='dog'):
    print("\nI have a "+animal_type+".")
    print("My "+ animal_type+"'s name is "+pet_name.title()+".")
describe_pet(pet_name='harry')

