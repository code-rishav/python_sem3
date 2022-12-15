reading1= open("file_handling/file1.txt","r")
reading2=open("file_handling/file2.txt","r")
writing=open("file_handling/file3.txt","w")

l1=reading1.readline()
l2=reading2.readline()
while(l1!="" or l2!=""):
    writing.write(l1.rstrip("\n")+l2.rstrip("\n"))
    writing.write("\n")
    l1=reading1.readline()
    l2=reading2.readline()

reading1.close()
reading2.close()
writing.close()