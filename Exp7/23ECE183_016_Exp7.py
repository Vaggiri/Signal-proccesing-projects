import numpy as np
import matplotlib.pyplot as plt

def convolve_signals(x, h):
    xlen=len(x)
    hlen=len(h)
    ylen=xlen+hlen -1
    y=np.zeros(ylen)
    for i in range(xlen):
        for j in range(hlen):
            y[i+j]+=x[i]*h[j]
    return y

n = np.linspace(-5,5,100)
Fc = 15
Fs = 85

x1 = 5*np.sin(2*np.pi*20*n + 0)
x2 = 10*np.sin(2*np.pi*40*n + 0)
x4 = x1 + x2
h = (np.sin(2*np.pi*(Fc/Fs)*n))/(np.pi*n)

y = convolve_signals(x4, h)
y1 = np.convolve(x4,h);

plt.figure(figsize=(10,8))

plt.subplot(231)
plt.stem(n,x1)
plt.title('x1[n]-CB.EN.U4ECE24016')
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(232)
plt.stem(n,x2)
plt.title('x2[n]-CB.EN.U4ECE24016')
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(233)
plt.stem(x4)
plt.title('x4[n]-CB.EN.U4ECE24016')
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(234)
plt.stem(h)
plt.title("h[n]-CB.EN.U4ECE24016")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(235)
plt.stem(y)
plt.title('y[n] Defined function-CB.EN.U4ECE24016')
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(236)
plt.stem(y1)
plt.title("y'[n] Built in function-CB.EN.U4ECE24016")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
