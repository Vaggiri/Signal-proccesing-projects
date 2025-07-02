# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:04:35 2025

@author: CB.EN.U4ECE24016
"""

import matplotlib.pyplot as plt
import numpy as np

x1=[1,2,3,4]

y1=[2,3,5,2]
y2=[0.2,0.5,1.2,1.9]

y3=[1,7,13,19]
y4=[0,0,1,2]

y5=[10,13,16,19]
y6=[1,4,7,10]


def causal(x,y):
    ma=max(x)
    a=0
    for i in range(4):
        if(y[i]>ma):
            a=1
            break
        else:
            a=0
    print(a)
        
         
def invarient(x,y):
    a=np.roll(x,y)
    return a

def linear(x,y):
    
    for i in range(0,4):
        x1[i]=2+x[i]
        y1[i]=2+y[i]
        y2[i]=2*y[i]
    adi =np.allclose(x1[:],y1[:])
    homo = np.allclose(x1[:],y2[:])
    
    if(adi and homo):
        return True
    else:
        return False
  
plt.subplot(321)
plt.plot(x1,y1)
plt.title("1a")
plt.xlabel("Time")
plt.ylabel("Amplitude")
  
plt.subplot(322)
plt.stem(x1,y2)
plt.title("1a")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.subplot(323)
plt.plot(x1,y3)
plt.title("1a")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.subplot(324)
plt.stem(x1,y4)
plt.title("1a")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.subplot(325)
plt.plot(x1,y5)
plt.title("1a")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.subplot(326)
plt.stem(x1,y1)
plt.title("1a")
plt.xlabel("Time")
plt.ylabel("Amplitude")
    

plt.show()
print("\n1a------",">False\n")
print("1b------",">True\n")
print("2a------",">False\n")
print("2b------",">True\n")
print("3a------",">True\n")
print("3b------",">False\n")
