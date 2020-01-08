#传递列表
def greet_users(names):
    for name in names:
        msg="Hello, " +name.title()+"!"
        print(msg)
usernames=['hannah','ty','margot']
greet_users(usernames)

#修改列表
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models=[]
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: "+ current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
print("\n")
#改进版本
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: "+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models=[]
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
print("\n")
#创建列表副本,在函数运行过程中不对原始列表进行更改
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models=[]
print_models(unprinted_designs[:],completed_models)
print("\n")
#传递任意数量的实参
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
#形参名*toppings中的星号  让Python创建一个名为toppings的   空元组  并将收到的所有值都封装到这个元组中

print("\n")
#改进版本
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("-"+topping)
make_pizza('mushrooms','green peppers','extra cheese') 
print("\n")

#使用任意数量的关键字参数
def build_profile(first,last,**user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('albert','einstein',location = 'princeton',field='physics')
print(user_profile)
#8-14
print("\n")
def make_car(brand,model,**other_info):
    car_info={}
    car_info['brand']=brand
    car_info['model']=model
    for key,value in other_info.items():
        car_info[key]=value
    return car_info
car=make_car('subaru','outback',color='blue',tow_package=True)
print(car)