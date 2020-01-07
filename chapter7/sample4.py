#用while循环来处理字典和列表
# 1 在列表之间移动元素
unconfirmed_users = ['alice','brian','candace']
confirmed_users =[]
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: "+ current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_users in confirmed_users:
    print(confirmed_users.title())

# 2 删除包含特定值的所有列表元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 3 使用用户输入来填充字典
responses = {}
polling_active =True
while polling_active:
    name=input("\nWhat is your name? ")
    response =input("which mountain would you like to climb someday? ")
    responses[name]=response
    repeat =input("Would you like to let another person respond? (yes/no) ")
    if repeat =='no':
        polling_active = False
print("\n---Poll Results---")
for name,response in responses.items():
    print(name +" would like to climb "+ response +".")

