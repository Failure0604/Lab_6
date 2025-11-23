from matplotlib.pyplot import *
from math import *

t = []
x = []
y = []

for i in range(400):
    t.append(i * 0.01)
    x.append(sin(2 * pi * t[i]))
    y.append(cos(2 * pi * t[i]))

plot(t, x)
plot(t, y)
savefig('sincos.png')
savefig('sincos.pdf')
show()