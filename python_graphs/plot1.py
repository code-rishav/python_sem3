import matplotlib.pyplot as plt

x2 = [10,20,30]
y2 = [20,40,10]
plt.plot(x2,y2,'b',label = 'line2')

x1 = [10,20,30]
y1 = [40,10,30]
plt.plot(x1,y1,'g',label = 'line1')


plt.legend()
plt.xlim(10,30)
plt.ylim(10,40)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("Two or more lines on same plot with suitable legends")
plt.show()