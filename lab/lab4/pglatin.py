# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 18:04:04 2020

@author: Harry
"""
ifilename = "war_and_peace.txt"
wfilename = "pglatin.txt"
infile = open(ifilename,'r')
outfile = open(wfilename,'w')
for line in infile:
    list_line = line.split()
    for word in list_line:
        n = len(word)
        print(word[1:n]+word[0]+"ay",end= " ",file=outfile)
    print("",file=outfile)