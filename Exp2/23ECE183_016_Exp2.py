import matplotlib.pyplot as plt
import numpy as np

plt.subplot(3,1,1)
t11=[-20,-15]
y11=[-20,-20]
plt.step(t11,y11)
plt.stem(t11,y11)
t22=[-10,-5,0,5,10]
y22=[0,-10,0,10,0]
plt.plot(t22,y22)
t33=[20,15]
y33=[20,20]
plt.title("x8(t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.step(t33,y33)
plt.stem(t33,y33)



A1=5  # Amplitude of Cosine
A2=10  # Amplitude of sine
f1=150 # Frequency of Cosine
f2=200 # Frequency of sine
the1=45 # Phase shift of Cosine
the2=0 # Phase shift of sine
rad =0.017453292519943295  # one radian Value 
t=np.linspace(0,0.1,1000)
y1 = A1*np.cos(2*np.pi*f1*t + (rad*the1)) # cos
y2 = A2*np.sin(2*np.pi*f2*t + (rad*the2)) # sin
y = y1+y2
plt.subplot(3,1,2)
plt.plot(t,y,label="x9(t)")
plt.title("x9(t)  Super impose")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()



c1 =5
c2 =10
fc1=50
fc2=100
c1t=0
c2t=0
t1=np.linspace(0,0.1,1000)
y3 = c1*np.exp(1j*2*np.pi*fc1*t1)
y4 = c1*np.exp(1j*2*np.pi*fc2*t1)

yr=np.real(y3+y4)
yi=np.imag(y4+y3)


plt.subplot(3,1,3)
plt.plot(t1,yr,label="Real")
plt.plot(t1,yi,label="Imaginery" ,linestyle=":")
plt.title("x10(t) Complex")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.show()
plt.tight_layout()
