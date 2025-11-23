from numpy import *
from matplotlib.pyplot import *

rcParams['font.sans-serif'] = ['Arial']

x = arange(0, 2.2, 0.2)

y1 = [0, 10, 24, 39, 55, 73, 87, 130, 140, 150, 200]
y2 = [0, 11, 25, 41, 58, 66, 94, 135, 140, 160, 170]
y3 = [0, 10, 24, 40, 57, 70, 90, 130, 145, 160, 180]

y = column_stack([y1, y2, y3])

errorbar(x, mean (y, axis = 1), yerr = [std(y, axis=1), std(y, axis=1)], marker='.', color='black')

title('Вольт-амперная характеристика')
xlabel('Напряжение, В')
ylabel('Ток, мкА')

show()