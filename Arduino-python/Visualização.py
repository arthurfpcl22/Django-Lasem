from Serial import ser
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_vals=[]
y_vals=[]
arduinoData=[]
i=0
index=count()
def animate(i):
	arduinoData.append(ser.readline().decode('utf-8'))
	if len(arduinoData)<2:
		pass
		
	else:
		x_vals.append(next(index))
		y_vals.append(float(arduinoData[i]))
		plt.cla()
		plt.plot(x_vals,y_vals)
		plt.title("Medições estilo")
		plt.xlabel("Tempo real",fontsize=14)
		plt.ylabel("Temperatura",fontsize=14)
		plt.tick_params(axis="both",labelsize=14)
		plt.ylim((0,35))
		plt.grid(color='g', linestyle='--', linewidth=0.5)
	i+=1
	
	
ani=FuncAnimation(plt.gcf(),animate,interval=1500)
plt.show()	
