from numpy import *
from matplotlib.pyplot import *
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['Arial']

t = arange(-1, 1, 0.01)
x = t**2
y = t**3
z = t**4

plot(t, x, label=r'$x^2$')
plot(t, y, '--', label=r'$x^3$')
plot(t, z, ':', label=r'$x^4$')

legend()
title('Степенные одночлены')
show()