from random import uniform, normalvariate
from matplotlib.pyplot import *

v = []
for i in range(10000):
    v.append(uniform(0, 6))
subplot(1, 2, 1)
hist(v)

w = []
for i in range(10000):
    w.append(normalvariate(0, 3)) 
subplot(1, 2, 2)
hist(w)  

show()