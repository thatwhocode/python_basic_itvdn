

class Transport():
    def move(self):
        return "Transport is moving"
    
class Bike(Transport):
    def move(self):
        return "Bike is riding"
class  Car(Transport):
    def move(self):
        return "Car is driving"

class Airplane(Transport):
    def move(self):
        return "Airplane is flying"
    
if __name__ == '__main__':
    car = Car()
    bike = Bike()
    airplane = Airplane()
    
    transports = [car, bike, airplane]
    for transport in transports:
        print(transport.move())        
    