def frequency(s):
    d={}
    for i in s:
        if i.isalpha():
            if i in d:
                d[i]+=1
            else:
                d[i]=1
    return d

name=input("Enter the string : ")
a=frequency(name.lower())
print("Letter\tFrequency")
for i in a:
    print(i,"\t",a[i])