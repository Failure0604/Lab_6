from numpy import *
from matplotlib.pyplot import *

x = arange(0, 10, 0.01)

f1 = exp(-x) * sin(2 * pi * x)
f2 = exp(-x) * sin(2 * pi * x + pi / 6)
f3 = exp(-x) * sin(2 * pi * x + pi / 3)

plot(x, f1, label=r'$\sin(2\pi x)$')
plot(x, f2, label=r'$\sin(2\pi x + \pi/6)$')
plot(x, f3, label=r'$\sin(2\pi x + \pi/3)$')

legend(loc='best')
grid(True)
show()