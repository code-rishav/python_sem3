from cmath import log10
import matplotlib.pyplot as plt
x = [i for i in range(2,21)]
y1 = [log10(i) for i in x]
plt.subplot(2,2,1)
plt.plot(x,y1,'r-')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("log")

y2 = [1/log10(i) for i in x]
plt.subplot(2,2,2)
plt.plot(x,y2,'k--')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("inverse log")

y3 = [2*i for i in x]
plt.subplot(2,2,3)
plt.plot(x,y3,'b.')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("linear")

y3 = [i*i for i in x]
plt.subplot(2,2,4)
plt.plot(y3,x,'m*')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("square")

plt.show()
plt.subplots_adjust(bottom=2.5, right=0.8, top=0.9,wspace=1,hspace=1)
plt.tight_layout(pad=2)