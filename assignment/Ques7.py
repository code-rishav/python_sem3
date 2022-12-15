def maximum(s1, s2, s3):
    if s1 > s2 and s1 > s3:
        return s1
    elif s2 > s3:
        return s2
    else:
        return s3


def vowel(s1):
    s = ""
    for i in s1:
        if i in "aeiou":
            s += "#"
        else:
            s += i
    return s


def wordCount(s1):
    count=0
    if s1 == "":
        return 0
    else:
        for i in s1:
            if i == " ":
                count += 1
        return count


def palindrome(s1):
    j = -1
    for i in s1:
        if (s1[j] != i):
            return False
        j -= 1
    return True


while (True):
    print()
    print("Press 1 to Find the length of string ")
    print("Press 2 to Return maximum of three strings ")
    print("Press 3 to replace all vowels with '#' in a string ")
    print("Press 4 to Find number of words in the given string ")
    print("Press 5 to Check whether the string is a palindrome or not ")
    print("Press Any Other Key to Exit : ")
    print()

    choice = int(input("Enter you choice : "))
    if choice == 1:
        string = input("Enter the string : ")
        print("Length of string is : ", len(string))
    elif choice == 2:
        string1 = input("Enter string 1 : ")
        string2 = input("Enter string 2 : ")
        string3 = input("Enter string 3 : ")
        print("Maximum string is : ", maximum(string1, string2, string3))
    elif choice == 3:
        string = input("Enter the string : ")
        print("string after replacing vowel with '#' is : ", vowel(string))
    elif choice == 4:
        string = input("Enter the string : ")
        print("Number of word in the string : ", wordCount(string))
    elif choice == 5:
        string = input("Enter the string : ")
        if string == "":
            print("String is empty ")
        elif palindrome(string):
            print("yes, the Given String is palindrome!! ")
        else:
            print("No, this string is not palindorme")
    else:
        break
