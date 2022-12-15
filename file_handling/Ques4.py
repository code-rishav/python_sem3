reading= open("file_handling/file1.txt","r")

d={}
l=reading.readlines()
for i in l:
    for j in i.split():
        if j.lower() not in d:
            d[j.lower()]=len(j)

max=0
for i in d:
    if d[i]>max:
        max=d[i]

print("Longest word are : ")
for i in d:
    if d[i]==max:
        print(i,end=" ")
reading.close()