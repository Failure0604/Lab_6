from numpy import *
from matplotlib.pyplot import *

x = arange(0, 10, 0.1)
f = exp(-x) * sin(2 * pi * x)
plot(x, f)
show()