from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D

x = arange(-3, 3, 0.5)  # от -3 до 3 (включительно), шаг 0.05
y = arange(-3, 3, 0.5)
X, Y = meshgrid(x, y)

# функция z = tan(x*y)
Z = tan(X * Y)

# закрашенная контурная диаграмма
figure(figsize=(8, 6))
contourf(X, Y, Z, levels=50, cmap='viridis')
colorbar()
title('Закрашенная контурная диаграмма: $z = \\tan(xy)$')
xlabel('x')
ylabel('y')
savefig('контурная_диаграмма_69_23.png')

# трёхмерный график
fig = figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)
colorbar(surf, shrink=0.5)
ax.set_title('Трёхмерный график: $z = \\tan(xy)$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_box_aspect([1,1,1])
savefig('трёхмерный_график_69_23.png')

show()