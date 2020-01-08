#返回值
def get_formatted_name(first_name,last_name):
    full_name=first_name + ' ' +last_name
    return full_name.title()

musician = get_formatted_name('jimi','handrix')
print(musician)

#返回字典
def build_person(first_name,last_name,age =''):
    #age作为可选参数，python认为非空字符串为true
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician = build_person('jimi','hendrix',age=27)
print(musician)

#结合使用函数和while循环
def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name =='q':
        break
    l_name =input("Last name: ")
    if l_name =='q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, "+ formatted_name+ '!')

#8-7
def make_album(singer,album,num=''):
    singer_album ={singer:album}
    if num:
        singer_album['number']=num
    return singer_album
Whynot = make_album('songxu','Whynot',12)
print(Whynot)

while True:
    print("\nPlease tell me the information about the album")
    print("(enter 'q' at any time to quit)")
    singer_name = input("Please enter the singer of the album: ")
    if singer_name =='q':
        break
    album_name = input("Please enter the name of the album: ")
    if album_name=='q':
        break
    num = input("Do you know the number of songs this album has, if you know enter the number, otherwise just press enter: ")
    Album=make_album(singer_name,album_name,num)
    print(Album)