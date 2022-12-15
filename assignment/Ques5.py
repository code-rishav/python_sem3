from fact import factorial

x=int(input("Enter the value of x : "))
n=int(input("Enter the value of n : "))

assert n>0,"Value of n must be greater than 0"

sum=0
for i in range(0,n+1):
    if(i%2==0):
        term = -(x**i)/factorial(i)
        sum-=term
    else:
        term = (x**i)/factorial(i)
        sum+=term
    print(term," ,",end=" ")
print()

print("Sum of terms:",sum)


