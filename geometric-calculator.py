###### Frederick Wittman
###### Dr. Hill
###### COSC 2030-01
###### 1 April 2019

import math

class Geometric_Calculator_Triangle:
    
    def __init__(self, side1, side2, side3):
        self.polygon = "Triangle"
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def calculate_triangle_perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def calculate_triangle_area(self):
        p = self.calculate_triangle_perimeter() / 2
        equation = p * (p - self.side1) * (p - self.side2) * (p - self.side3)
        area = math.sqrt(equation)
        return area
    
    def print_triangle(self):
        print("The perimeter of the triangle is " + str(self.calculate_triangle_perimeter()) + ".")
        print("The area of the triangle is " + str(self.calculate_triangle_area()) + ".\n")

class Geometric_Calculator_Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def calculate_rectangle_perimeter(self):
        perimeter = (2 * self.length) + (2 * self.width)
        return perimeter
        
    def calculate_rectangle_area (self):
        area = self.width * self.length
        return area
    
    def print_rectangle(self):
        print("The perimeter of the rectangle is " + str(self.calculate_rectangle_perimeter()) + ".")
        print("The area of the rectangle is " + str(self.calculate_rectangle_area()) + ".\n")
        

class Geometric_Calculator_Diamond:

    # The angle is in radians.  We only need one angle because we know the internal angles add to 360 degrees.  Also, the sine of 
    # the internal angles is the same.
    
    def __init__(self, side, angle):
        self.side = side
        self.angle = angle
    def calculate_diamond_perimeter(self):
        perimeter = 4 * self.side
        return perimeter
        
    def calculate_diamond_area (self):
            area = (self.side ** 2) * (math.sin(self.angle)) 
            return area
    
    def print_diamond(self):
        print("The perimeter of the diamond is " + str(self.calculate_diamond_perimeter()) + ".")
        print("The area of the diamond is " + str(self.calculate_diamond_area()) + ".\n")
        
tri = Geometric_Calculator_Triangle(3, 4, 5)
rect = Geometric_Calculator_Rectangle(4, 5)
diam = Geometric_Calculator_Diamond(4, math.pi / 2)

tri.print_triangle()
rect.print_rectangle()
diam.print_diamond()

tri.side1 = 8
rect.length = 8
diam.angle = math.pi / 4

print("\n")
tri.print_triangle()
rect.print_rectangle()
diam.print_diamond()

        
        

