#将函数储存在模块中
def make_pizza(size,*topping):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings: ")
    for topping in topping:
        print("-"+topping)