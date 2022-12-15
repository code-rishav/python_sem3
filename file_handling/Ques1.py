reading= open("file_handling/file2.txt","r")
writing=open("file_handling/sourcecopy.txt","w")

l=reading.readlines()
for i in l:
    writing.write(i.rstrip("\n"))

reading.close()
writing.close()