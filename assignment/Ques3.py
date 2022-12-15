def fibonacci(n):
    if (n==1 or n==0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def factorial(n):
    product=1
    for i in range (1,n+1):
        product*=i
    return product

def main():
    num=int(input("Enter the number : "))
    l=[fibonacci(num),factorial(fibonacci(num))]
    print("Fibonacci of number",num,": ",l[0])
    print("Factorial of ",l[0],": ",l[1])

main()