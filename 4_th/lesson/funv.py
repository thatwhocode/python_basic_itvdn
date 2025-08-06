from double_woof import Cat, Dog, DoubleWoofDog


def describe_pet(pet):
    print(f"Pet`s name is {pet.name}",f"and it says {pet.speak()}")


if __name__ =="__main__":
    cat = Cat("Garfield")
    dog = Dog("Peter")
    second_dog = DoubleWoofDog("Arnold")
    my_animals=  [cat, dog, second_dog]
    for animal in my_animals:
        describe_pet(animal)