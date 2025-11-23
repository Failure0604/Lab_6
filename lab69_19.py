from numpy import *
from matplotlib.pyplot import *
# График функции 2: x^3 на [-2, 2], меняю шаг выборки данных на 0.5
x = arange(-2, 2.01, 0.5)
y1 = x**3

subplot(2, 1, 1)
plot(x, y1, '--o', color='pink', linewidth=2, markersize=6)  # Розовая пунктирная линия с кружками
title(r'$y = x^3$')
xlabel('x')
ylabel('y')
grid(True)
# График функции 7: 4*sin(πt + π/8) - 1 на [-10, 10], меняю шаг выборки данных на 0.5
t = arange(-10, 10.01, 0.5)
y2 = 4 * sin(pi * t + pi / 8) - 1

subplot(2, 1, 2)
plot(t, y2, '-.s', color='green', linewidth=2, markersize=6)  # Зелёная штрихпунктирная линия с квадратами
title(r'$y = 4 \sin(\pi t + \pi/8) - 1$')
xlabel('t')
ylabel('y')
grid(True)

tight_layout()

savefig('69_19.png') 
savefig('69_19.pdf')  
savefig('69_19.jpg') 
savefig('69_19.eps')   

show()