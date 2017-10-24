import csv
import matplotlib.pyplot as plt
data = csv.reader(open('2d_data.csv', 'rb'), delimiter=",", quotechar='|')
column1, column2 = [], []

for row in data:
    column1.append(row[0])
    column2.append(row[1])

print column1
print column2
labels = column1
sizes = column2

fig1, ax1 = plt.subplots()
ax1.pie(sizes,  labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
