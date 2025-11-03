#2. Implement a constructor to initialize attributes for a `Car` class.
class Car:
    def __init__(self,name,color):
        self.name=name
        self.__color=color#The color cannot be accesible to edit or change directly (Beacuse it is private attribute)
    
    def show_name(self):
        print(f"The name of the car is {self.name}")
    
    def is_color(self):
        print(f"The color of the {self.name} is {self.__color}")
    
car1=Car("Alto","Black")
car2=Car("S","D")
car1.show_name()
car1.color="Blue"#Tried to change the color of the car it is not changed 
car1.is_color()
car2.is_color()