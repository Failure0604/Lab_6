from numpy import *
from matplotlib.pyplot import *

x = arange(-1, 1.01, 0.01)
colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']

for n in range(1, 7):
    subplot(3, 2, n)  # 2 столбца
    y = x**n
    plot(x, y, color=colors[n-1], linewidth=2)
    title(f'$y = x^{n}$')
    xlabel('x')
    ylabel('y')
    grid(True)

tight_layout()
savefig('два_столбца.png')
show()