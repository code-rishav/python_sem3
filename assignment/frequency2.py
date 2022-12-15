def exact_match(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    count = 0
    for i in str1:
        count += str2.count(i)
    print("Total count of characters considering all the repeatition is: ",count)
def match(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str3=''
    count =0
    for i in str1:
        if(i not in str3):
            str3+=i
    for j in str3:
        count+= str2.count(j)
    print("Total count after not considering repaeating elements: ",count)

str1 = 'abhrajhk'
str2 = 'this is python programming language and python is fun'
exact_match(str1,str2)
match(str1,str2)

