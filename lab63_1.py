from numpy import *
from matplotlib.pyplot import *

# Генерируем данные
t = arange(0, 2, 0.01)
x = sqrt(t)
y = t
z = sqrt(t**3)
u = t**2 
v = sqrt(t**5)
w = t**3

subplot(3, 2, 1)
plot(t, x, label='x**(1/2)')
title(r'$\sqrt{x}$')
ylim([0, 5])

subplot(3, 2, 2)
plot(t, y, label='x', color='red')
title(r'$x$')
ylim([0, 5])

subplot(3, 2, 3)
plot(t, z, label='x**(3/2)')
title(r'$\sqrt{x^3}$')
ylim([0, 5])

tight_layout()

show()