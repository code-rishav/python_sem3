from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

x2 = np.linspace(10,20,50)+ np.linspace(20,30,50) # [10,20,30]
y2 = np.linspace(20,40,50)+np.linspace(40,10,50) #[20,40,10]
plt.plot(x2,y2,'rs',label = 'line2')

x1 = np.linspace(10,20,50)+np.linspace(20,30,50) #[10,20,30]
y1 = np.linspace(40,10,50)+np.linspace(10,30,50) #[40,10,30]
plt.plot(x1,y1,'b.',label = 'line1')

plt.legend()
plt.xlim(10,30)
plt.ylim(10,40)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Two or more lines on same plot with suitable legends")
plt.show()