from matplotlib.pyplot import plot, show
from math import pi, sin 

t = []
x = []

for i in range(400):
    t.append(i * 0.01)
    x.append(sin(2 * pi * t[i]))

plot(t, x, color = 'grey')
show()