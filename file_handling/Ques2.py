reading= open("file_handling/file1.txt","r")
writing=open("file_handling/dest.txt","w")

l=reading.readlines()
for i in l:
    writing.write(i)

reading.close()
writing.close()