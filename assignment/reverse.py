def recursion(str,rev,i):
    if(i==-1):
        return str[-1]
    rev+= recursion(str,rev,i+1)+ str[i]
    return rev

def non_recursive(str):
    str2=''
    for i in range(length-1,-1,-1):
        str2+=str[i]
    return str2


str = 'this is a python program'
length = len(str)
rev = ''
rev = recursion(str,rev,-length)
print("Revesed string by using recursion is: ",rev)
print("Reversed string by using non-recursion is: ",non_recursive(str))
