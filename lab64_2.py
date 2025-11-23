from numpy import *
from random import normalvariate
from matplotlib.pyplot import *

data1 = []
data2 = []
data3 = []

for i in range(10):
    data1.append(normalvariate(5, 0.5))
    data2.append(normalvariate(5, 0.5))
    data3.append(normalvariate(5, 0.5))

locs = arange(1, len(data1) + 1) 
width = 0.2  

bar(locs, data1, width=width, color='blue')
bar(locs + width, data2, width=width, color='red')
bar(locs + 2 * width, data3, width=width, color='green')

xticks(locs + width * 1.5, locs) 

show()