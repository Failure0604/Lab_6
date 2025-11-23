# исходный код был нерабочий, поэтому я его немного исправила
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure(figsize=(8, 6))

ax = fig.add_subplot(111, projection='3d')

ax.grid(True)

show()