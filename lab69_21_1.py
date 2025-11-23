from numpy import *
from matplotlib.pyplot import *

x = arange(-1, 1.01, 0.01)
colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']

for n in range(1, 7):
    subplot(6, 1, n)  # в 1 столбец
    y = x**n
    plot(x, y, color=colors[n-1], linewidth=2)
    title(f'$y = x^{n}$')  # название вместо легенды
    xlabel('x')
    ylabel('y')
    grid(True)

tight_layout()
savefig('один_столбец.png')
show()