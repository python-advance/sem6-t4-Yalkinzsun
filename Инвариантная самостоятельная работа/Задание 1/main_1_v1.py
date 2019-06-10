import numpy as np
import matplotlib.pyplot as plt
import csv

Y1, Y2, names = [], [], []

with open("property_prices.csv") as file:
    reader = csv.reader(file, delimiter=',')
    for line in reader:
        names.append(line[0])
        Y1.append(int(line[1]))
        Y2.append(int(line[2]))


xs = range(len(names))

fig, ax = plt.subplots()
index = np.arange(len(names))
bar_width = 0.30

plt.scatter(xs, Y1, label=u'2-комнатные квартиры', color='y')
plt.scatter(xs, Y2, label=u'3-комнатные квартиры', color='k')

plt.xlabel('Районы Санкт-Петербурга')
plt.ylabel('Стоимость квартиры')
plt.title('Мин. стоимость 2- и 3-комнатных квартир по районом СПб\n(10.06.19, Яндекс.Недвижимость)\n')
plt.xticks(xs, names)
fig.autofmt_xdate(rotation=45)
plt.legend()

plt.show()
