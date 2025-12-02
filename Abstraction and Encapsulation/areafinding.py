#5. Create a class Rectangle with methods to calculate area and perimeter. Overload constructors.
class rectangle:
    def __init__(self,len,bred):
        self.len=len
        self.bred=bred
    def area(self):
        print(f"Area of rectangle is {self.len*self.bred}")
    def perimeter(self):
        print(f"Perimeter of rectangle is {2*(self.len+self.bred)}")
a=rectangle(2,4)
a.area()
a.perimeter()
        