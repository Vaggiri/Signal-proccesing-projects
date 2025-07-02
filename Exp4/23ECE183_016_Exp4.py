import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

t=np.arange(0,45,5)



x1=[0,20,0,0,0,20,0,0,0]
a=(4*t-10 + (t/5))
plt.subplot(3,2,1)
plt.plot(a,x1)
plt.title("x4(t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.subplot(3,2,2)
plt.stem(a,x1)
plt.title("x4(t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.tight_layout()


xp = [0, 10, 10.001, 20, 20.001, 30, 30.001,40]
yp = [0, 1, 0, 1, 0, -1, 0,0]

plt.subplot(3,2,3)
plt.plot(xp,yp)

plt.show()

