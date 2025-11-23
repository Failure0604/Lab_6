from numpy import *
from matplotlib.pyplot import *

x = arange(-1, 1.01, 0.01)

colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']

for n in range(1, 7):
    y = x**n
    plot(x, y, color=colors[n-1], linewidth=2, label=f'$x^{n}$')

title('Семейство степенных функций $x^n$, n=1..6')
xlabel('x')
ylabel('y')

tight_layout()

show()