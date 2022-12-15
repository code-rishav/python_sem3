writing= open("file_handling/file1.txt","w")

num=int(input("How many numbers you want to enter : "))
for i in range(num):
    n=int(input("Enter number : "))
    writing.write(str(n)+"\n")
writing.close()

reading= open("file_handling/file1.txt","r")
sum=0
l=reading.readlines()
for i in l:
    num=int(i.rstrip("\n"))
    if num%2==1:
        sum+=num

print("Sum of odd numbers are : ",sum)
reading.close()
writing.close()