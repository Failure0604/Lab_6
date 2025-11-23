from numpy import *
from matplotlib.pyplot import *

t = arange(0, 1, 0.001) 
x = sin (10*pi*t)    
y = t 
z = sqrt (t**3) 

figure (1)
plot(t, y) 

figure (2)
plot(t, z) 

figure (3)
plot(t, x)

show()