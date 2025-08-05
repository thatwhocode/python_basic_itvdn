from amoeba import Amoeba
class Lancelet(Amoeba):
    organization ="multi-cell"
    support = "notochord"
    @classmethod
    def describe(cls):
        description = super().describe()
        return description + f". It has {cls.support} for support"
    @staticmethod
    def move(direction):
        print(f"Move ot {direction} with muscles")
    def eat (self, subject):
        print(f"{self.name.capitalize()} filters water to eat{subject}")
        
if __name__ == '__main__':
    print(Lancelet.describe())
    
    
    lancelet = Lancelet("Amphioxus")
    lancelet.move("right")
    lancelet.eat(" organical particles")