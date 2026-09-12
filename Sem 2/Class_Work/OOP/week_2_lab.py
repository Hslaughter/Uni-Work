import math

class HelloWorld:
    def greet(self):
        name = input("Enter your name: ")
        print(f"hi {name}, hello object world")

greeter = HelloWorld()
greeter.greet() 

class Circle:
    def __init__(self, a, b, radius, angle):
        self.a = a
        self.b = b
        self.radius = radius
        self.angle = angle

    def circumference(self):
        result = 2*self.radius*math.pi
        return result

    def area(self):
        result = self.radius*self.radius*math.pi
        return result

    def coordinate(self):
        x = self.radius*math.cos(self.angle) + self.a
        y = self.radius*math.sin(self.angle) + self.b
        result = f"{x}, {y}"
        return result




a = int(input("Please enter a value for a: "))
b = int(input("Please enter a value for b: "))
radius = int(input("Please enter the radius: "))
angle = int(input("Please enter the angle: "))

circle = Circle(a,b,radius,angle)

circumference = circle.circumference()
area = circle.area()
coord = circle.coordinate()

print(f"The area of the circle is {area} and the circumference is {circumference}")
print(f"The coordinates of your circle are {coord}")