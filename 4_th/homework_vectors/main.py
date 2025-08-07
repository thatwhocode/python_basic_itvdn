from typing import Optional


class Vector2D():
    def __init__(self, x:int | float, y: int|float)->None:
        self.x = x
        self.y = y
    def __add__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        else:
            return Vector2D(self.x + other.x, self.y + other.y)
    def __str__(self):
        print(f"Vector wiht values {self.x, self.y}")


class Vector3D(Vector2D):
    def __init__(self, x: int | float, y: int | float, z: Optional[int | float]) -> None:
        super().__init__(x, y)
        self.z = z 
    def __add__(self, other):
        new_2d = super().__add__(other)
        new_x, new_y = new_2d.x, new_2d.y
        
        new_z = None
        if isinstance(other, Vector3D):
            if self.z is not None and other.z is not None:
                new_z = self.z + other.z
        
        
        return Vector3D(new_x, new_y, new_z)
        
    def  __str__(self):
        return f"Vector with elements {self.x, self.y, self.z}"
    

if __name__ == "__main__":
    vec_1, vec_2 = Vector2D(1,1), Vector2D(2,2)
    vec_3 = Vector3D(1,1,0)
    print(vec_3)
    