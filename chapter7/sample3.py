current_number = 1
while current_number <=5:
    print(current_number)
    current_number+=1

prompt = "\nTell me something, and I will repeat it back to you"
prompt +="\nEnter 'quit' to end the program "

active= True#使用标志，在任何事件导致标志的值为False时让程序停止运行
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)

#break立即退出while循环不再运行循环中余下的代码
while True:
    city=input("Please enter the name of the city you have visited enter 'quit' when you are finished ")
    if city == 'quit':
        break
    else:
        print(city.title())

#continue返回循环开头
current_number=0
while current_number<10:
    current_number+=1
    if current_number %2 ==0:
        continue
    print(current_number)