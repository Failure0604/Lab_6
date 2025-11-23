from numpy import *
from matplotlib.pyplot import *

x = arange(0, 10, 0.01)

f1 = exp(-x) * sin(2 * pi * x)
f2 = exp(-x) * sin(2 * pi * x + pi / 6)
f3 = exp(-x) * sin(2 * pi * x + pi / 3)

subplot(3, 1, 1)
plot(x, f1)
title(r'$\sin(2\pi x)$')
grid(True)

subplot(3, 1, 2)
plot(x, f2)
title(r'$\sin(2\pi x + \pi/6)$')
grid(True)

subplot(3, 1, 3)
plot(x, f3)
title(r'$\sin(2\pi x + \pi/3)$')
grid(True)

tight_layout()
show()