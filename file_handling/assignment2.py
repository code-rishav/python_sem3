def numbers():
    l = []
    while True:
        num = int(input("Enter a number"))
        if num >100:
            break
        l.append(num)
    return l
def file(l):
    f = open("file_handling/numbers.txt","a")
    for i in l:
        f.write(str(i)+" ")
    f.close()

def maxmin():
    f = open("file_handling/numbers.txt","r")
    max,min = 100000,-100000
    l = []
    for i in f:
        l = i.split()
    print("content of the file:")
    for j in l:
        j = int(j)
        print(j,end=" ")
        if j>max:
            max = j
        if j<min:
            min = j
    print("Maximum: ",max,"Minimum:",min)
    if max-min>40:
        raise RuntimeError("Difference greater than 40")

def main():
    lst = numbers()
    v = file(lst)
    maxmin()

main()
        


    