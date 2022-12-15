def highest(name,marks):
    avg = sum(marks)/4
    global highest_marks
    global student
    if(avg> highest_marks):
        highest_marks = avg
        student = name 
    
d={}
student=""
highest_marks=0
 #to keep the highest marks updated
while(True):
    print()
    print("Press 1 to Enter the detail of student ")
    print("Press 2 to Find the name of the student securing highest percentage :")
    print("Press Any Other Key to Quit")
    print()

    choice = int(input("Enter you choice : "))

    if choice == 1:
        name=input("Enter name of the Student ")
        if name in d:
            print("This student already exist !!")
        else:
            sub1=float(input("Enter marks of subject 1 : "))
            sub2=float(input("Enter marks of subject 2 : "))
            sub3=float(input("Enter marks of subject 3 : "))
            sub4=float(input("Enter marks of subject 4 : "))
            marks = [sub1,sub2,sub3,sub4]
            d[name]= marks
            highest(name,marks)
            print("Student added ")

    elif choice == 2:
            print("Highest Average marks is sceured by ",student,"having average of: ",highest_marks)
    else:
        break

