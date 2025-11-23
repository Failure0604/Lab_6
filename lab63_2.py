from numpy import *
from matplotlib.pyplot import *

rcParams['font.sans-serif'] = ['Arial']

t = arange(0, 10, 0.001) 
x = cos (2*pi*t)    
y = cos (20*2*pi*t) 
z = (1+0.7*x)*y  

subplot(2, 2, 1) 
plot(t[:2000], x[:2000], color='black') 
title('Модулирующий сигнал')
xlabel('Time, s')
ylabel('Voltage, V')

subplot(2, 2, 2) 
plot(t[:2000], y[:2000], color='black')
title('Несущий сигнал')
xlabel('Time, s')
ylabel('Voltage, V')

subplot(2, 1, 2)
plot(t, z, color='black')
title('AM-сигнал')
xlabel('Time, s')
ylabel('Voltage, V')

tight_layout()

show()