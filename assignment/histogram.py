import matplotlib.pyplot as plt
def inputList():
    ls = []
    length = int(input('Enter the length of list: '))
    for i in range(0, length, 1):
        ls.append(int(input('Enter element {}:'.format(i+1))))
    return ls
if __name__ == "__main__":
    list = inputList()
    plt.hist(list, )
    plt.xlabel('Integer')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.savefig('hist.png', dpi=275, bbox_inches='tight') # To save the plot
    plt.show()
