import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-1, 1.0, 0.001)
x = np.sin(2 * np.pi * t)
y = np.cos(5 * np.pi * t)

plt.figure(1, figsize=(8, 3)) 
plt.plot(t, x)
plt.ylabel('sin(t)')

plt.figure(2)
plt.plot(t, y)
plt.ylabel('cos(t)')

plt.figure(1)     
plt.grid(True)

plt.show()