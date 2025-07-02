# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:47:37 2025

@author: CB.EN.U4ECE24016
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

t=np.linspace(-3,3,1000)
x2a=signal.square(2*np.pi*3*t)
plt.subplot(2,1,1)
plt.axvline(0,color="black")
plt.axhline(0,color="black")
plt.plot(t,x2a)

sample_rate = 1000
per_rate = int((1/3)*sample_rate)
periodic = np.allclose(x2a[:per_rate],x2a[per_rate:2*per_rate],atol=1e-5)



t1=[-0.1,-0.10,0,0.1,0.1]
x2b=[0,1,1,1,0]
plt.subplot(2,1,2)
plt.axvline(0,color="black")
plt.axhline(0,color="black")
plt.plot(t1,x2b)

is_per =not periodic and (np.var(x2a)>0)
is_per2 =not(not periodic and (np.var(x2b)>0))

if(is_per):
    print("The Signal x2a(t) is Periodic Siganl")
else:
    print("The Signal x2a(t) is Aperiodic Siganl")

if(is_per2):
    print("The Signal x2b(t) is Periodic Siganl")
else:
    print("The Signal x2b(t) is Aperiodic Siganl")