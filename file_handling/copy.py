src = open('file_handling/source_c.txt','r')
content = src.readlines()
dest = open("file_handling/dest.txt",'w')
for i in content:
    dest.write(i)
src.close()
dest.close()