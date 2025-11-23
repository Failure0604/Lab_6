# исходный код был нерабочий, поэтому я его немного исправила
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = figure(figsize=(8, 6))

ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 50) 
v = np.linspace(0, np.pi, 50)    

x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones_like(u), np.cos(v))

ax.plot_surface(x, y, z, color='grey', alpha=0.7)

savefig('3D.png')

show()