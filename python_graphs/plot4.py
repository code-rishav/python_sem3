import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,6,20)
y1 = [i for i in x]
y2 = [i**2 for i in x]
y3 = [i**3 for i in x]

plt.plot(x,y3,"r^")
plt.plot(x,y2,"bs")
plt.plot(x,y1,"g--")

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Display marker")
plt.show()

