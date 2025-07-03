# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 14:00:35 2025

@author: CB.EN.U4ECE24016
"""

import matplotlib.pyplot as plt
import numpy as np

def dtfs(N,x):
    c=np.zeros(N,dtype=complex)
    for k in range(N):
        for n in range(N):
            c[k]+=x[n]*np.exp((-2j*np.pi/N)*n*k)
        c[k]/=N
    return c
N=8
x1=[]
x2=[]
for n in range(N): 
    val1=1+np.cos((np.pi/4)*n)
    x1.append(val1)
    
for n in range(N):
    val2=(2*np.cos((4*np.pi*n/5) + (np.pi/3))) + (3*np.sin(6*np.pi*n/5))
    x2.append(val2)
    
x1=np.array(x1)
x2=np.array(x2)



coefficient=dtfs(N,x1)
magnitude=np.abs(coefficient)
phase=np.angle(coefficient)

coefficient2=dtfs(N,x2)
magnitude2=np.abs(coefficient2)
phase2=np.angle(coefficient2)


for i in range(N):
    print(f"coefficient[{i}] = {coefficient[i].real}  {coefficient[i].imag}j | "f"Magnitude = {magnitude[i]} Phase = {phase[i]}\n")
print("______________________________________________________________________________________________________________________________\n")   
for i in range(N):
    print(f"coefficient2[{i}] = {coefficient2[i].real}  {coefficient2[i].imag}j | "f"Magnitude = {magnitude2[i]} Phase = {phase2[i]}\n")

plt.figure(figsize=(10,10))  

plt.subplot(321)
plt.stem(range(N),x1)
plt.title("x1[n]")
plt.xlabel("k")
plt.ylabel("Amplitude")
plt.grid()
 
plt.subplot(324)
plt.stem(range(N),magnitude)
plt.xlabel("k")
plt.ylabel("|x[n]|")
plt.grid()

plt.subplot(326)
plt.stem(range(N),phase)
plt.title("x1[n]-----Phase")
plt.xlabel("k")
plt.ylabel("Phase")
plt.grid()

plt.subplot(322)
plt.stem(range(N),x2)
plt.title("x2[n]")
plt.xlabel("k")
plt.ylabel("Amplitude")
plt.grid() 
   
plt.subplot(323)
plt.stem(range(N),magnitude2)
plt.title("x2[n]-------Magnitude")
plt.xlabel("k")
plt.ylabel("|x[n]|")
plt.grid()

plt.subplot(325)
plt.stem(range(N),phase2)
plt.title("x2[n]----------Phase")
plt.xlabel("k")
plt.ylabel("Phase")
plt.grid()

plt.tight_layout()
plt.show()

