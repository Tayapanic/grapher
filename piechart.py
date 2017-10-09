import matplotlib.pyplot as plt
n = input("input number of labels:")
ar = []
ar2 = []
ar3 = []
for i in range(n):
	ar.append(raw_input("name of the label :" ))
	ar2.append(raw_input("percentage :" ))
	ar3.append(0)
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ar
sizes = ar2
explode = ar3  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
