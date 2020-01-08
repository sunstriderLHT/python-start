def make_car(brand,model,**other_info):
    car_info={}
    car_info['brand']=brand
    car_info['model']=model
    for key,value in other_info.items():
        car_info[key]=value
    return car_info
car=make_car('subaru','outback',color='blue',tow_package=True)
print(car)