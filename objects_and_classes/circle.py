import math

class Circle:
    def __init__(self,radius=1):
        self.radius = radius
    
    def getPerimeter(self):
        return 2*self.radius*math.pi
    
    def getArea(self):
        return math.pi*(self.radius**2)
    
    def setRadius(self,radius):
        self.radius = radius
