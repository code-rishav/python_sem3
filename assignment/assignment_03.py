class Demo:
    def __init__(self):
        self.s = ""
    def Get_String(self):
        self.s = input("Enter the string: ")
    def Print_String(self):
        print("String in upper case")
        print(self.s.upper())

if __name__=="__main__":
    p = Demo()
    p.Get_String()
    p.Print_String()
