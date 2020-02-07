# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:50:22 2020

@author: Harry
"""

Birth_stone =['Garnet',
 'Amethyst',
 'Aquamarine',
 'Diamond',
 'Emerald',
 'Pearl',
 'Ruby',
 'Peridot',
 'Sapphire',
 'Opal',
 'Topaz',
 'Turquoise']    

def birthstone():
    month = input("Please enter the month number you were born:")
    
    birthstone = Birth_stone[int(month)-1]
    print("Your birthstone is: "+birthstone)
    

def cipher():
    
    message = input("Please enter the message you want to encrypted: ")
    key = input("Please enter your key: ")
    m_list =list(message.replace(" ",""))
    for i in range(len(m_list)):
        m_list[i]= chr(int(ord((m_list[i]))-65+int(key))%26+65)
    
    for letter in m_list:
        
        print(letter,end="")


def reverse(message_n):
    message_r=[]
    for i in message_n.split():
        
        message_r.append(i[::-1])
    
    message_str = " ".join(message_r)
    return message_str

 

def backwards_diary():
    infileName = "diary.txt"
    outfileName = "reverse.txt"
    
    infile = open(infileName,'r')
    outfile = open(outfileName,'w')
    
    file = infile.read()
    r_file = reverse(file)
    
    print(r_file,file = outfile)
    
    infile.close()
    outfile.close()    
        
        


def main():
    birthstone() 
    cipher()
    print("\nIf I did not know the key, I would try 1-26 as key to decrypt")
    message_n =input("Please enter the message you want to encrypted: ")
    print(reverse(message_n))
    backwards_diary()
main()

