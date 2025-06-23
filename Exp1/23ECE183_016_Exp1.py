import matplotlib.pyplot as plt
import numpy as np

def unit(n):
	return np.where(n>=0,10,0)
n = np.arange(-10,10)
step = unit(n)
plt.figure(figsize=(10,10))
plt.subplot(211)
plt.stem(n,step)
plt.subplot(212)
plt.plot(n,step)
plt.xlabel("n")
plt.ylabel("u(n)")
plt.grid()
plt.title("Unit Step Signal")
plt.show()