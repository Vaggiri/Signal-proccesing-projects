# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:48:11 2025

@author: CB.EN.U4ECE24016
"""

import matplotlib.pyplot as plt
import numpy as np

t1=np.arange(-10,10.001,0.01)
t=np.linspace(0,1,1000)

x3a=np.exp(-(t1*t1))

x3b=10*np.cos(2*np.pi*10*t+np.radians(90))

plt.subplot(2,1,1)
plt.axvline(0,color="black")
plt.axhline(0,color="black")
plt.title("x3a")
plt.plot(t1,x3a)
plt.subplot(2,1,2)
plt.axvline(0,color="black")
plt.axhline(0,color="black")
plt.title("x3b")
plt.plot(t,x3b)

energy1=np.sum(np.abs(x3a)**2)
power1=np.mean(np.abs(x3a)**2)

energy2=np.sum(np.abs(x3b)**2)
power2=np.mean(np.abs(x3b)**2)

if(energy1>power1):
    print("The signal x3a is Power Signal")
else:
    print("The signal x3a is Energy Signal")
    
if(energy2>power2):
    print("The signal x3b is Energy Signal\n\n")
else:
    print("The signal x3b is Power Signal\n\n")

print("x3a Power = ",power1)
print("x3a Energy = ",energy1)

print("x3b Power = ",power2)
print("x3b Energy = ",energy2)
