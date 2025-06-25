import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
t=np.linspace(0,0.1,1000)
x1=10*np.sin(2*np.pi*100*t+(np.radians(180)))
x2=5*signal.sawtooth(2*np.pi*200*t,0.5)

y9=(5*x1)-(10*x2)
y10=(0.7*x1)*(10*x1)
ys=np.gradient(x2,t)
y11= ys + (0.5*x1)

plt.figure(figsize=(20,20))
plt.subplot(4,2,1)
plt.plot(t,x1,label="Input wave 1")
plt.plot(t,x2,label="Input wave 2")
plt.title("Input wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()


plt.subplot(4,2,3)
plt.plot(t,y9)
plt.title("y9(t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")



plt.subplot(4,2,5)
plt.plot(t,y10)
plt.title("y10(t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.subplot(4,2,7)
plt.plot(t,y11)
plt.title("y11(t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()
#------------------------------------

plt.subplot(4,2,2)
plt.stem(t,x1,label="Input wave 1")
plt.stem(t,x2,label="Input wave 2")
plt.title("Input wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()


plt.subplot(4,2,4)
plt.stem(t,y9)
plt.title("y9(t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")


plt.subplot(4,2,6)
plt.stem(t,y10)
plt.title("y10(t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")


plt.subplot(4,2,8)
plt.stem(t,y11)
plt.title("y11(t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()