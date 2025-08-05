# Спадкування -механізм який дозволяє наслідувати а також перевизанчати методи базового(батьківського) класу


class Amoeba:
    organization ="single-cell"
    habitation = "water"
    
    def __init__(self, name):
        self.name  = name
    @classmethod 
    def describe(cls):
        return(f"{cls.__name__} has {cls.organization} and lives in {cls.habitation}")
    @staticmethod
    def move(direction):
        print (f"Moves to the {direction} with pseudoposia")
    def eat(self, subject):
        print(f"{self.name.capitalize()} grows psudopodia ", f"to eat {subject}")
    
    
if __name__ == '__main__':
    print(Amoeba.describe())
    amoeba = Amoeba("proteus")
    amoeba.move("left")
    amoeba.eat("bacteria")