# Implement a `Shape` class and derive `Circle` and `Rectangle` classes with a method
# `calculate_area`. Each class should calculate area differently based on its shape.
#   - Create a loop to calculate areas for both `Circle` and `Rectangle` objects.
class shape:
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (3.14)*(self.radius**2)
class rectangle(shape):
    def __init__(self,len,bre):
        self.len=len
        self.bre=bre
    def area(self):
        return self.len*self.bre
shapes=[circle(3),rectangle(2,3)]
for shape in shapes:
    print("area:",shape.area())

