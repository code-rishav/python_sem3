import matplotlib.pyplot as plt
x = [i for i in range(11)]
c = 3
m = 1
y = [(m*i+c) for i in x]
plt.plot(x,y,'g+-',linewidth='1.5')
plt.xlabel('X values')
plt.ylabel('y values')
plt.title("Linear dependency")
plt.show()