import numpy as np
import matplotlib.pyplot as plt

def convolve(x4, h):
    len_x4 = len(x4)
    len_h = len(h)
    len_y = len_x4 + len_h - 1
    y = np.zeros(len_y)

    # Perform the convolution
    for n in range(len_y):
        for k in range(len_x4):
            if 0 <= n - k < len_h:
                y[n] += x4[k] * h[n - k] 
    return y

n = np.linspace(-5,5,100)
n1 = np.linspace(-10, 10, 50)
ts = 1/2500

def h(n, fc, fs):
    h = np.sin(2*np.pi*(fc/fs)*n)/(np.pi*n)
    return h

x1 = 10*np.sin(2*np.pi*100*n) + 5*np.sin(2*np.pi*900*n)
x11 = 10*np.sin(2*np.pi*100*n1) + 5*np.sin(2*np.pi*900*n1)

x2 = 10*np.sin(2*np.pi*200*n) + 5*np.sin(2*np.pi*1000*n) + 10*np.sin(2*np.pi*0*n)
x22 = 10*np.sin(2*np.pi*200*n1) + 5*np.sin(2*np.pi*1000*n1) + 10*np.sin(2*np.pi*0*n1)



h11 = h(n1, 500, 2500)
h22 = h(n1, 600, 2500)



y11 = convolve(x11, h11)
y22 = convolve(x22, h22)


x3 = y11 + y22
h3 = h(n1, 400, 2500)
y3 = convolve(x3, h3)

heq = convolve(h11+h22, h3)
xeq = x11 + x22
xeq1 = x1 + x2

yeq = convolve(xeq, heq)



# Plot the signals
plt.figure(figsize=(20, 20))
plt.suptitle("Experiment 9 - Interconnection of Systems")



plt.subplot(4, 3, 1)
plt.stem(ts*np.arange(len(x1)), x1)
plt.title("x1[n] - CB.EN.U4ECE24030")
plt.xlabel("n")
plt.ylabel("x1[n]")

plt.subplot(4, 3, 2)
plt.stem(ts*np.arange(len(h11)), h11)
plt.title("h1[n] - CB.EN.U4ECE24030")
plt.xlabel("n")
plt.ylabel("h1[n]")

plt.subplot(4, 3, 3)
plt.stem(ts*np.arange(len(y11)), y11)
plt.title("y1[n] - CB.EN.U4ECE24030")
plt.xlabel("n")
plt.ylabel("y1[n]")


plt.subplot(4, 3, 4)
plt.stem(ts*np.arange(len(x2)), x2)
plt.title("x2[n] - CB.EN.U4ECE24030")
plt.xlabel("n")
plt.ylabel("x1[n]")

plt.subplot(4, 3, 5)
plt.stem(ts*np.arange(len(h22)), h22)
plt.title("h2[n] - CB.EN.U4ECE24030")
plt.xlabel("n")
plt.ylabel("h2[n]")

plt.subplot(4, 3, 6)
plt.stem(ts*np.arange(len(y22)), y22)
plt.title("y2[n] - CB.EN.U4ECE24030")
plt.xlabel("n")
plt.ylabel("y2[n]")

plt.subplot(4, 3, 7)
plt.stem(ts*np.arange(len(x3)), x3)
plt.title("x3[n] - CB.EN.U4ECE24030")
plt.xlabel("n")
plt.ylabel("x3[n]")

plt.subplot(4, 3, 8)
plt.stem(ts*np.arange(len(h3)), h3)
plt.title("h3[n] - CB.EN.U4ECE24030")
plt.xlabel("n")
plt.ylabel("h3[n]")

plt.subplot(4, 3, 9)
plt.stem(ts*np.arange(len(y3)), y3)
plt.title("y3[n] - CB.EN.U4ECE24030")
plt.xlabel("n")
plt.ylabel("y3[n]")

plt.subplot(4, 3, 10)
plt.stem(ts*np.arange(len(xeq1)), xeq1)
plt.title("x'[n] - CB.EN.U4ECE24030")
plt.xlabel("n")
plt.ylabel("x'[n]")

plt.subplot(4, 3, 11)
plt.stem(ts*np.arange(len(heq)), heq)
plt.title("h'[n] - CB.EN.U4ECE24030")
plt.xlabel("n")
plt.ylabel("h'[n]")

plt.subplot(4, 3, 12)
plt.stem(ts*np.arange(len(yeq)), yeq)
plt.title("y'[n] - CB.EN.U4ECE24030")
plt.xlabel("n")
plt.ylabel("y'   [n]")


plt.tight_layout()
plt.show()