from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Создаём фигуру
fig = figure()

# Добавляем 3D-оси
ax = Axes3D(fig)

# Генерируем данные
u = np.linspace(0, 2 * np.pi, 100)  # Угол по горизонтали (φ)
v = np.linspace(0, np.pi, 100)       # Угол по вертикали (θ)

# Вычисляем координаты x, y, z для поверхности (сфера или тор)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

# Строим поверхность
ax.plot_surface(x, y, z, color='grey')

# Сохраняем график
savefig('3D.png', dpi=150, bbox_inches='tight')

# Показываем
show()