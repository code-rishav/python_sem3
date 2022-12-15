def remove_newline(content,write_f):
    for i in content:
        write_f.write(i.rstrip())
    return 
def main():
    read_f = open('file_handling/source.txt','r')
    write_f = open('file_handling/source.txt','w')
    source_content = read_f.readlines()
    remove_newline(source_content)
    read_f.close()
    write_f.close()
main()
