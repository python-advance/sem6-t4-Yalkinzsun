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

fig, ax = plt.subplots()
index = np.arange(len(names))
bar_width = 0.30

rects1 = plt.bar(index, Y1, bar_width,
                 alpha=0.8,
                 color='y',
                 label='2-комнатные квартиры')

rects2 = plt.bar(index + bar_width, Y2, bar_width,
                 alpha=0.8,
                 color='k',
                 label='3-комнатные квартиры')

plt.xlabel('\nРайоны Санкт-Петербурга')
plt.ylabel('Стоимость квартиры\n')
plt.title('Мин. стоимость 2- и 3-комнатных квартир по районом СПб\n(10.06.19, Яндекс.Недвижимость)\n')
plt.xticks(range(len(names)), names)
fig.autofmt_xdate(rotation=45)
plt.legend()
plt.show()
