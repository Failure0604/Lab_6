from random import uniform, normalvariate
from matplotlib.pyplot import *

v = []
for i in range(10000):
    v.append(uniform(0, 6))
subplot(1, 2, 1)
hist(v, bins = 100, density=True) #normed параметр больше не поддерживается, заменила на density

w = []
for i in range(10000):
    w.append(normalvariate(0, 3)) 
subplot(1, 2, 2)
hist(w, bins= 100, density=True)  

show()