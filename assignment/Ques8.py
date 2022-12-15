def checkNum(l):
    for i in l:
        if not i.isnumeric():
            return False
    return True


def odd(l):
    count = 0
    for i in l:
        if int(i) % 2 != 0:
            count += 1
    return count


def largestString(l):
    s = ""
    for i in l:
        if i > s:
            s = i
    return s


def reverse(l):
    temp = []
    for i in range(-1, -len(l)-1, -1):
        temp.append(l[i])
    return temp


def findEle(l, element):
    for i in range(0, len(l)):
        if element == l[i]:
            return i
    return -1


def removeEle(l, element):
    while (element in l):
        l.remove(element)


def sort(l):
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j] < l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]


def commonMember(l1, l2):
    l3 = []
    for i in l1:
        if i in l2 and i not in l3:
            l3.append(i)
    return l3


def main():
    l = []
    size = int(input("Enter size of List : "))
    for i in range(size):
        l.append(input("Enter element : "))

    while (True):
        print()
        print("Press 1 to Check if all elements are numbers")
        print("Press 2 to Count odd numbers if list is numeric")
        print("Press 3 to Display largest string in list")
        print("Press 4 to Reverse the list")
        print("Press 5 to Find item in list")
        print("Press 6 to Remove item from list")
        print("Press 7 to Sort in Descending order")
        print("Press 8 to Find common elements from another list")
        print("Press Any Other Key to Quit")
        print()

        choice = int(input("Enter you choice : "))

        if choice == 1:
            if (checkNum(l)):
                print("Yes all the elements of the list are numeric ")
            else:
                print("All the elements of the list are not numeric ")

        elif choice == 2:
            if (checkNum(l)):
                print("Number of odd number in the list : ", odd(l))
            else:
                print("The given list is numeric")

        elif choice == 3:
            print("Largest string the list : ", largestString(l))

        elif choice == 4:
            print("List after reversing the list is : ", reverse(l))

        elif choice == 5:
            element = input("Enter the element to find : ")
            check = findEle(l, element)
            if (check == -1):
                print("Element not present in the list")
            else:
                print("Element is present at index : ", check)

        elif choice == 6:
            element = input("Enter the element to remove : ")
            removeEle(l, element)
            print("List after removing", element, "is : ", l)

        elif choice == 7:
            sort(l)
            print("List after sorting in descending order is : ", l)

        elif choice == 8:
            l2 = []
            size2 = int(input("Enter size of Another List : "))
            for i in range(size2):
                l2.append(input("Enter element : "))
            l3 = commonMember(l, l2)
            print("Common member in Both list are : ")
            for i in l3:
                print(i, end=" ")

        else:
            break


main()
