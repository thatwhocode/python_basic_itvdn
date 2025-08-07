from random import randint

class Vehicle():
    def __init__(self, mark : str, model: str) -> None:
        self.mark = mark
        self.model = model
        self._mileage = randint(100, 100000)
        
    def update_mileage(self, num: int) -> None:
        if num>0:
            self._mileage+= num
        else: 
            raise ValueError("Mileage can not be negative")
    def get_mileage(self):
        return self._mileage
    def get_details(self):
        return f"Vehicle mark is {self.mark}, vehicle model is {self.model}, mileage is {self.get_mileage()} "
    
    
    
if __name__ == '__name__':
    skoda = Vehicle("Skoda", "Octavia")
    print(skoda.get_mileage())
    try:
        skoda.update_mileage(-100)
    except ValueError:
        print ("Wrong mileage")
    else: 
        print("Succesfully added mileage")
    try:
        skoda.update_mileage(100)
    except ValueError:
        print ("Wrong mileage")
    else: 
        print("Succesfully added mileage")
    print(skoda.get_mileage())
    print(skoda.get_details())