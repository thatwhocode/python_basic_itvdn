
# should be asctract?
class Shape(): 
    name =  "Base class name"
    def area(self):
        return 0
    
class  Rectangle(Shape):
    name = " Rectangle"
    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width
        if (width<=0):
            raise ValueError("Width should be positive")
        if(self.height<=0):
            raise ValueError("Height should be positive")
        
    def area(self):
        return self.width * self.height 

class Circle(Shape):
    name = "Circle"
    def __init__(self, radius):
        self.radius = radius
        if(radius <= 0):
            raise ValueError("Radius of circle should be positive")       
        
    def area(self):
        return 3.1415926*self.radius**2
            

