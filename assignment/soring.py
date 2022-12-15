import time

def selection(l):
    initial = time.time()
    min = 0
    for i in range(0,len(l)):
        min = i
        j = i+1
        while(j<len(l)):
            if(l[j]<l[min]):
                min = j
            j = j+1
        l[i],l[min] = l[min],l[i]
    final = time.time()
    units = final-initial
    return l,units
def insertion(l):
    initial = time.time()
    for i in range(len(l)):
        index = l[i]
        j = i-1
        while(j>=0 and l[j]>index):
            l[j+1] = l[j]
            j-=1
        l[j+1] = index
    final = time.time()
    units = final - initial
    return l,units

def bubble(l):
    initial = time.time()
    for i in range(len(l)):
        for j in range(0,len(l)-1-i):
            if (l[j] > l[j + 1]):
                l[j],l[j+1] = l[j+1],l[j]
    final = time.time()
    units = final - initial
    return l,units

def sort_list(l):
    print("FOR LIST")
    l,t = insertion(l)
    print("INSERTION SORT: ",l," | time: ",t," micro seconds")
    l,t = selection(l)
    print("SELECTION SORT: ",l," | time: ",t," micro seconds")
    l,t = bubble(l)
    print("BUBBLE SORT: ",l," | time: ",t," micro seconds")

def sort_tuple(t):
    print("FOR TUPLE: ")
    l1,t = selection(list(t))
    l1 = tuple(l1)
    print("SELECTION SORT: ",l1," | time: ",t," micro seconds")
    l2,t = insertion(list(t))
    l2 = tuple(l2)
    print("INSERTION SORT: ",l2," | time: ",t," micro seconds")
    l3,t = bubble(list(t))
    l3 = tuple(l3)
    print("BUBBLE SORT: ",l3," | time: ",t," micro seconds")


            
def main():
    lst = [14,5,3,7,3,7,9,3,9,7]
    sort_list(lst)
    tup = tuple([12,34,56,78,90,32,54,76,98])
    sort_tuple(tup)
main()



        