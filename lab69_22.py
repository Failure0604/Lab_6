from matplotlib.pyplot import *

# всего 19 человек
data = [2, 6, 8, 3]
labels = [
    'Одни пятёрки',
    'Пятёрки и четвёрки',
    'С тройками, без задолженностей',
    'С задолженностями, но пересдали'
]

colors = ['pink', 'green', 'yellow', 'lightblue']

figure(figsize=(8, 6))
pie(data,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    shadow=True,
    startangle=90)

axis('equal')
title('Итоги сессии 19 человек')

show()