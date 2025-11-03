#Create a class where a student’s marks cannot 
# be accessed directly but can be updated or viewed only using methods.
class student:
    def __init__(self,marks):
        self.__marks=marks
    def update(self,mark):
        if mark>=0:
           self.__marks+=mark
        if mark<0:
           self.__marks+=mark
    def view(self):
        print(f"The student current marks is {self.__marks}")
s=student(100)
s.update(12)
s.update(-99)
s.view()