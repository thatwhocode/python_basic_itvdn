class Animal():
    def __init__(self, name: str)-> None:
        self.name = name
    @staticmethod
    def speak():
        pass

class Dog(Animal):
    @staticmethod
    def speak():
        return"Woof"
class Cat(Animal):
    @staticmethod
    def speak():
        return"Meow"
    
if __name__=="__main__":
    my_dog = Dog("Red beard")
    my_cat = Cat("Alex")


    my_animals=[my_dog, my_cat]

    for animal in my_animals:
        print(animal.speak())