class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        sum=0
        for i in self.marks:
            sum+=i
        print(f"The average of {self.name} is {(sum)/len(self.marks)}")
        
    
a=student("John",[123,21,34,5,54])
a.average()
b=student("Dany",[54,123,21,34,5])
b.average()