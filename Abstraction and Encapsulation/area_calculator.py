class area:
    def __init__ (self):
       pass
   
    def rectangle(self,len,brea):
        print(f"The Area of rectangle is {len*brea} sq.cms")
    def square(self,len):
        print(f"The Area of the square is {len**2} sq.cms")
    def circle(self,len):
        print(f"The Area of the circle is {3.14*((len)**2)}")
c=area()
c.rectangle(12,13)
c.square(3)
c.circle(3)