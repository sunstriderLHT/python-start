# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 13:38:42 2020

@author: Harry
"""
import math
import numpy as np
from matplotlib import pyplot as plt

# Q1

def area(r_mile):
    km = r_mile*1.60934
    area = round(math.pi*(km)**2,2)
    return area

# Q2

def mag(A1,A0):
    magnitude = round(math.log(A1,10)-math.log(A0,10),1)
    return magnitude

# Q3
    
def convert_time(time_24):
    if time_24%12==0:
        time_12 = 12
    else:
        time_12 = time_24%12
    return time_12

# Q4
    
def distance(a,b):
    distance = round(np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2),2)
    return distance

# Q5

def quantization(float_array,step_size):
    q_array = [step_size*np.floor(floats/step_size+0.5) for floats in float_array]
    return q_array

# Q6

def seismo_tremor():
    time_slot = [time/2 for time in range(0,101)]
    tremor = [2*np.sin(time+0.5)+5 for time in time_slot]
    q_tremor = quantization(tremor,3)
    plt.title("seismograph tremor in 50 seconds")
    plt.xlabel("time")
    plt.ylabel("q_tremor") 
    plt.scatter(time_slot,q_tremor,s=10)
    plt.show()
    
    
def main():
    print("Richter scale level: "+str(mag(60400,0.005)))
    print("Distance to the earthquake: "+str(distance(np.array([100,30]),np.array([-50,150]))))
    print("Total area affected by the earthquake: "+str(area(500)))
    print("Time of the earthquake: "+str(convert_time(20))+":30")
    seismo_tremor()
    
    
    
    
    