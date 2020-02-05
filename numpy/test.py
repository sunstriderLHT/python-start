# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:52:52 2020

@author: Harry
"""
class Solution():
    def compress(self,chars):
        count =0
        new_list = []
        for item in chars:
            
            if item in new_list:
                count+=1
                
            else:
                if len(new_list) ==0:
                    new_list.append(item)
                    count= 1
                
                else:
                    if count!=1:
                        for char in str(count):
                            new_list.append(char)
                        
                    new_list.append(item)    
                    count = 1
        if count!=1:
            for char in str(count):
                new_list.append(char)
        chars = new_list       
        print(new_list)
        print(chars)       
solution = Solution()                
solution.compress(["a","a","b","b","c","c","c"])
            

