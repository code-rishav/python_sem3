def frequency(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    for i in str1:
        count = 0
        count = str2.count(i)
        print("frequency of ",i,'is: ',count)

str1 = 'abphog'
str2 = 'thiS Is a Python program'
frequency(str1,str2)


