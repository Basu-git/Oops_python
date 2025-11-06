#Write a program to create a calculator which is capable of finding squares,cubes and sqroot
    
class exp:
    def __init__(self,num):
        self.num=num
    def sq(self):
        print(self.num**2)
    def cube(self):
        print(self.num**3)
        
    def root(self):
        print(self.num**(1/2))
n=exp(2)
n.sq()
n.cube()
m=exp(9)
m.root()
        