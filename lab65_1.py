from matplotlib.pyplot import *

data = [18, 15, 11, 9, 8, 6]
labels = ['Java', 'C', 'C++', 'PHP', 'Python', 'Ruby']
explode = [0, 0, 0, 0, 0.2, 0] 

axes(aspect=1)

pie(data, labels=labels, explode=explode,
    autopct='%1.1f%%', shadow=True) 

show()