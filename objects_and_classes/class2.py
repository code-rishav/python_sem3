class Dog:
# Class Variable

    animal = "dog"

    # The init method or constructor
    def __init__(self, breed, color):
        # Instance Variable
        self.breed = breed
        self.color = color

# Objects of Dog class
Rodger = Dog("dog","brown")
Buzo = Dog("Bulldog","black")

print("Rodger detail")
print('Rodeger is a',Rodger.animal)
print("Bredd: ",Rodger.breed)
print("Color:", Rodger.color)

print("Buzo details:")
print("Buzo is ", Buzo.animal)
print("Breed: ", Buzo.breed)
print("Color:", Buzo.color)

# Class variables can be accessed using class
# name also
print("Accessing class variable using class name")
print(Dog.animal)