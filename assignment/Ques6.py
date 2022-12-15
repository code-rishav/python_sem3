def even(t1):
    l=[]
    for i in t1:
        if i%2==0:
            l.append(i)
    t=tuple(l)
    return t

def concat(t1,t2):
    t3=t1+t2
    return t3
    
def max_min(t):
    max=min=t[0]
    for i in t:
        if(i>max):
            max=i
        elif(i<min):
            min=i
    return max,min

def main():
    t1=(1,2,5,7,9,2,4,6,8,10)

    t2=even(t1)
    print("Tuple with even elements is : ",t2)

    t3=(11,13,15)
    t1=concat(t1,t3)
    print("Tuple after concatination : ",t1)

    max,min=max_min(t1)
    print("Maximum element is : ",max)
    print("Minimum element is : ",min)

main()