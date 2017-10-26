import matplotlib.pyplot as plt
def func(n):
	#n = input("input number of labels:")
	#ar = []
	ar2 = []
	ar3 = []
	for i in range(eval(n)):
		#ar.append(input("name of the label :" ))
		ar2.append(input("percentage :" ))
		ar3.append(0)
	# Pie chart, where the slices will be ordered and plotted counter-clockwise:
	#labels = ar
	sizes = ar2
	explode = ar3  # an array corresponding t which elemnts should be exploded. right now no element

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, autopct='%1.1f%%',
	        shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	#fig=plt.figure()
	plt.plot()
	fig1.savefig('./static/polls/test.png')
	plt.show()
n=input()
func(n)
