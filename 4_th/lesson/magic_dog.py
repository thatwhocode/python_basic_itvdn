from funv import Dog, DoubleWoofDog, describe_pet


class MagicDog(Dog):
    def __add__(self, other):
        return MagicDog(f"Puppy (love of {self.name} and {other.name})")
    def __str__(self):
        return f"Tis is {self.name}, and it says {self.speak()} inside magic method"
    


if __name__ == '__main__':
    first_dog = MagicDog("Peter")
    second_dog = MagicDog("Alice")
    third_dog = first_dog + second_dog
    fourth_dog = DoubleWoofDog("Arnold")

    my_animals = [first_dog, second_dog, third_dog, fourth_dog]
    for animal in my_animals:
        print( animal)