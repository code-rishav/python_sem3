from circle import Circle
def main():
    circle1 = Circle()
    print("The area of Circle is: ",circle1.getArea())
    circle2 = Circle(25)
    print("The area of circle with radius ",circle2.radius,"is: ",circle2.getArea())
    circle2.setRadius(20)
    print("The area of circle with radius ",circle2.radius,"is: ",circle2.getArea())
main()