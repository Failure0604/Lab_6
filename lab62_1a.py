from numpy import *
from matplotlib.pyplot import *
from matplotlib import rcParams

t = arange (0, 4, 0.01)
x = sin (2*pi*t)
y = cos (2*pi*t)

plot(t, x, t, y)

title('Voltage over time')
xlabel('Time, s')
ylabel('Voltage, V')
show()