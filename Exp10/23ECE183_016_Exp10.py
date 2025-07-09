# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 13:59:54 2025

@author: CB.EN.U4ECE24016
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

t=np.arange(-0.5,0.5,0.0033)
x2= signal.square(2*np.pi*300*t)
def dtft(x,nop=100):
    n=np.arange(len(x))
    omega = np.linspace(-2*np.pi,2*np.pi,nop)
    X= np.array([np.sum(x*np.exp(-1j * w * n)) for w in omega])
    return omega,X


n=np.arange(-50,50)

x=[]


f=[100,200,300,400,500]
a=[2,4,0,1,6]
for i in range(1,6):
   phase=a[i-1]/5
   val = a[i-1]*np.cos(2*np.pi*f[i-1]*n + np.radians(phase))
   x.append(val)
x=np.array(x)
x1=[1.99995126,3.9996101,0,0.99999391,5.9986841]

omega,X=dtft(x1)
omega1,X1=dtft(x2)
plt.figure(1)
plt.subplot(312)
plt.stem(n*10,np.abs(X))
plt.title("Magnitude--Q1")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.subplot(313)
plt.stem(n*10,np.angle(X))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("Phase--Q1")
plt.subplot(311)
plt.stem(f,x1)
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("Input Signal--Q1")

plt.tight_layout()

plt.figure(2)
plt.subplot(312)
plt.stem(omega1,np.abs(X1))
plt.title("Magnitude--Q2")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.subplot(313)
plt.stem(omega1,np.angle(X1))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("Phase--Q2")
plt.subplot(311)
plt.stem(t,x2)
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("Input Signal--Q2")


plt.tight_layout()
plt.show()




