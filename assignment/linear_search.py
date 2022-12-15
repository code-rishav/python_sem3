import time
import math

def search1(l,ele):
    pos=0
    initial = time.time()
    for i in range(len(l)):
        if l[i] == ele:
            break
    final = time.time()
    units = final - initial
    return i,units

def search2(s,ele):
    found = False
    initial = time.time()
    for i in s:
        if i == ele:
            found = True
            break
    final = time.time()
    units = final - initial 
    units = final - initial
    round(units,2)
    return found,units

def search3(d,ele):
    found = False
    initial = time.time()
    for i in d:
        if d[i] == ele:
            found = True
            break
    final = time.time()
    units = final - initial 
    units = final - initial
    round(units,2)
    return found,units

def main():
    lst = [1,4,3,78,5,67,45,8,9,6,34,45,55,78,99,88,90]
    tup = (1,4,3,78,5,67,45,8,9,6,34,45,55,78,99,88,90)
    s = set((1,4,3,78,5,67,45,8,9,6,34,45,55,78,99,88,90))
    pos,t = search1(lst,45)
    print("For LIST element found at: ",pos,"and time takes was: ",t,'micro seconds')
    pos,t = search1(tup,78)
    print("For TUPLE element found at: ",pos,"and time takes was: ",t,'micro seconds')
    pos,t = search2(s,45)
    print("For SET element found at: ",pos,"and time takes was: ",t,'micro seconds')
    dic = {1:4,3:78,5:67,45:8,9:6,34:45,55:78,99:88}
    pos,t = search3(dic,1)
    print("For DICTIONARY element found at: ",pos,"and time takes was: ",t,'micro seconds')

main()
    


    