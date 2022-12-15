import math

class Circle:
    def __init__(self):
       self.radius = 0
    
    def get_radius(self):
        self.radius = float(input("Enter the radius: "))
    
    def calc_area(self):
        return math.pi*(self.radius**2)
    
if __name__=="__main__":
    c = Circle()
    c.get_radius()
    print("Area of Circle: ",c.calc_area())