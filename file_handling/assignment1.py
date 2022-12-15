def file():
    while True:
        try:
            f_name = input("Enter the file name")
            f_name = "file_handling/"+f_name
            infile = open(f_name,"r")
            return infile
        except IOError:
            print("File",f_name,"does not exist")
    

def count(lines):
    count = 0
    l = []
    for i in lines:
        l = i.split()
    for j in l:
        if j=='the' or j=="The":
            count = count+1
    return count

def main():
    content = file()
    print("No. of counts",count(content))

main()
