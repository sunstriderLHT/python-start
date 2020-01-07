num = input("please input a number ")
num = int(num)
if num%10 ==0:#%用于求余数，余数为0说明可以被整除
    print("this number can be divided by 10")
else:
    print("this number cannot be divided by 10")