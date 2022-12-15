import matplotlib.pyplot as plt

x = [1,4,5,6,7]
y = [2,6,3,6,3]

plt.plot(x,y,marker='o',linestyle='dashed',color='red',markerfacecolor='blue',markersize=12)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Display marker")
plt.show()