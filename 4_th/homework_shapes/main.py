


class Rectangle():
    def __init__(self, width:int|float, height: int | float):
        if width<=0  or height <= 0:
            raise ValueError
        else:
            self.width = width
            self.height = height
    
    
    def get_area(self)-> float:
        return float(self.width * self.height)
    


class Circle():
    def __init__(self, radius: int|float)-> None:
        if radius<= 0:
            raise ValueError
        else:
            self.radius = radius
    
    def get_area(self)-> float: 
        return 3.14 * (self.radius**2)
    
    

def get_area(shape):
    print(f"The area is {shape.get_area()}")


if __name__ =='__main__':
    rect = Rectangle(2,4)
    circle = Circle(3)
    get_area(rect)
    get_area(circle)