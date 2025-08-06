from animals import Dog, Cat

class DoubleWoofDog(Dog):
    @staticmethod
    def speak():
        return "Woof!Woof!"
    

if __name__ =="__main__":
    cat = Cat("Garfield")
    dog = Dog("Peter")
    second_dog = DoubleWoofDog("Arnold")
    my_animals=  [cat, dog, second_dog]
    for animal in my_animals:
        print(animal.speak())