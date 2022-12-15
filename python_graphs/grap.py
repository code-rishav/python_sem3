import matplotlib.pyplot as plt
x = [i for i in range(1,21)]
y1 = [i*i for i in x]
y2 = [(i*i*i) for i in x]
plt.plot(x,y1,'r*--',x,y2,'b*--')
#plt.plot(x,y2)
plt.show()
