def BinarySearch(l, element):
    start = 0
    end = len(l)
    while (start <= end):
        mid = (start+end)//2
        if (l[mid] == element):
            return mid
        elif (l[mid] > element):
            end = mid-1
        else:
            start = mid+1
    return -1


def LinearSearch(l, element):
    for i in range(0, len(l)):
        if l[i] == element:
            return i
    return -1

def insertionSort(l):
    for i in range(1,len(l)):
        check=l[i]
        j=i-1
        while(j>=0 and check<l[j]):
            l[j+1]=l[j]
            j-=1
        l[j+1]=check

def bubbleSort(l):
    for i in range(0,len(l)):
        for j in range(0,len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

def selectionSort(l):
    for i in range(0,len(l)):
        minimum=i
        for j in range(i+1,len(l)):
            if l[j]<l[minimum]:
                minimum=j
        l[i],l[minimum]=l[minimum],l[i]

def main():
    l = []
    size = int(input("Enter size of List : "))
    for i in range(size):
        l.append(input("Enter element : "))

    while (True):
        print()
        print("Press 1 to Search an element ")
        print("Press 2 to Sort the elements :")
        print("Press Any Other Key to Quit")
        print()

        choice = int(input("Enter you choice : "))

        if choice == 1:
            print()
            print("Press 1 to Search an element using Linear Search")
            print("Press 2 to Search an element using Binary Search")
            print()
            choice = int(input("Enter you choice : "))

            value = input("Enter element to be search : ")

            if choice == 1:
                check = LinearSearch(l, value)
                if check != -1:
                    print(value, "found at index", check)
                else:
                    print("element not found!!")

            elif choice == 2:
                check = BinarySearch(l, value)

                if check != -1:
                    print(value, "found at index", check)
                else:
                    print("element not found!!")

            else:
                print("You pressed a wrong option!!")

        elif choice == 2:
            print("Press 1 to sort List using Bubble Sort")
            print("Press 2 to sort List using Selection Sort")
            print("Press 3 to sort List using Insertion Sort")
            print()

            choice = int(input("Enter you choice : "))

            if choice == 1:
                bubbleSort(l)
                print("List after sorting using Bubble sort is : ",l)

            elif choice == 2:
                selectionSort(l)
                print("List after sorting using selection sort is : ",l)

            elif choice == 3:
                insertionSort(l)
                print("List after sorting using insertion sort is : ",l)

            else:
                print("Wrong input!!")            

        else:
            break

if __name__=="__main__":
    main()