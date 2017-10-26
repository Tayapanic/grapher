import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

def animate(i):
	graph_data = open('example.txt' ,'r').read()
	    
	lines = graph_data.split('\n')
	    
	xs=[]
	ys=[]
	        
	            
	            
	    
	for line in lines:
	    if len(line)>1:
	        x,y = line.split(',')
	        xs.append(float(x))
	            
	        ys.append(float(y))
	
	
	a=zip(xs,ys)
	a.sort(key=lambda x: x[0])

	

	xs1=[]
	ys1=[]

	for line in a:
	    if len(line)>1:
	        
	        xs1.append(line[0])
	            
	        ys1.append(line[1])
	
	ax1.clear()
	ax1.plot(xs1,ys1)

ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.show()
