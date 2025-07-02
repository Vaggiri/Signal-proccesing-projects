# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:03:57 2025

@author: CB.EN.U4ECE24016
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

t=[-10,-10,0,10,10]
t1=[10,10,0,-10,-10]
x1a=[0,20,0,20,0]

x1b=[0,-10,0,10,0]
    
    
plt.subplot(2,2,1)
plt.title("X1a(t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.axvline(0,color="black")
plt.axhline(0,color="black")
plt.plot(t,x1a)
plt.grid()
plt.subplot(2,2,3)
plt.axvline(0,color="black")
plt.axhline(0,color="black")
plt.title("X1b(t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(t,x1b)
plt.grid()
plt.subplot(2,2,2)
plt.axvline(0,color="black")
plt.axhline(0,color="black")
plt.title("X1a(t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(t1,x1a)
plt.grid()
plt.subplot(2,2,4)
plt.axvline(0,color="black")
plt.axhline(0,color="black")
plt.title("X1b(t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(t1,x1b)
plt.grid()
plt.tight_layout()
plt.show()

check_x1a = np.allclose(x1a,x1a[::-1])
check_x1b = np.allclose(x1b,x1b[::-1])

if (check_x1a):
    print("The Signal x1a(t) is Even Siganl")
else:
    print("The Signal x1a(t) is Odd Siganl")
    
if (check_x1b):
    print("The Signal x1b(t) is Even Siganl")
else:
    print("The Signal x1b(t) is Odd Siganl")