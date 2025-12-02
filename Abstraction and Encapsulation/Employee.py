#Design a class Employee to store name, id, salary. Add method to increase salary by percentage.
class employe:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def salary(self,sal):
        self.sal=sal
        print("The salary is ",self.sal)
    def increment(self,increment):
        print(f"The Salary after increment is {self.sal+self.sal*(increment/100)}")
a=employe("John",12)
a.salary(1500)
a.increment(14)
a.salary(1600)
a.increment(13)    