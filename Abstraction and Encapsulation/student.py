class student:
    def __init__(self,name):
        self.name=name
    def average(self,mark1,mark2,mark3):
        print(f"Average of {self.name} is {(mark1+mark2+mark3)/3}")
    
a=student("Jhon")
a.average(1,2,3)
b=student("Dany")
b.average(4,5,6)
        