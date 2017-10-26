import matplotlib.pyplot as plt,mpld3
import pandas as pd
def hist_func(data,title,xlabel,ylabel):
	#data = pd.read_csv('~/grapher-master/result.csv', sep=',',header=None, index_col =0)
	#fig_hist,axis_hist=plt.subplots()
	data.plot(kind='bar')
	plt.ylabel(str(ylabel))
	plt.xlabel(str(xlabel))
	plt.title(str(title))
	plt.plot()
	#print(data)
	plt.savefig('polls/static/polls/histogram.png')
	fig_hist=mpld3.fig_to_html(plt.figure(1))
	#mpld3.save_html(plt.figure(1),"test.html")
	plt.close()
	return fig_hist
	
#k=input()
#hist_func(k)
