x = 'y'
lst = []
while(x=='y'):
    num = int(input("Enter the number: "))
    assert num>=0 and num<=100, "Number should be between 0 and 100"
    lst.append(num)
    x = input("Do you want to continue: y/n ")
for i in range(0,101):
    count = lst.count(i)
    if(count!=0):
        print("Frequency of ",i,"is :",count)