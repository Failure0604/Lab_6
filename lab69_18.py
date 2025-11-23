from numpy import *
from matplotlib.pyplot import *

# График функции 2: x^3 на [-2, 2]
x = arange(-2, 2, 0.1)
y1 = x**3

subplot(2, 1, 1)
plot(x, y1)
title(r'$y = x^3$')
xlabel('x')
ylabel('y')
grid(True)

# График функции 7: 4*sin(πt + π/8) - 1 на [-10, 10] 
t = arange(-10, 10, 0.1) 
y2 = 4 * sin(pi * t + pi / 8) - 1

subplot(2, 1, 2)
plot(t, y2)
title(r'$y = 4 \sin(\pi t + \pi/8) - 1$')
xlabel('t')
ylabel('y')
grid(True)

tight_layout()

show()