from .main import Shape, Rectangle, Circle
shape = Shape()
rect  = Rectangle(2,2)
circle = Circle(3)
def test_shape_creation():
    assert shape.area() == 0
def test_rect_area():
    assert rect.area() == 2*2
    assert rect.height == 2
    assert rect.width == 2 
    assert rect.name == " Rectangle"
def test_circle_area():
    assert circle.radius == 3
    assert circle.name == "Circle"
    assert circle.area() == 3.1415926*circle.radius**2