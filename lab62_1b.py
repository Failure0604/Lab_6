from numpy import *
from matplotlib.pyplot import *
from matplotlib import rcParams

t = arange (0, 4, 0.01)
x = sin (2*pi*t)
y = cos (2*pi*t)

plot(t, x, t, y)

title('Voltage over time')
xlabel(r'$t$, c', fontsize = 18)
ylabel(r'$E_{cm}$, B, $i_{c}$, мкА', fontsize = 18)
show()