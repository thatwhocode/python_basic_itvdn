from lancelet import Lancelet

class Clownfish(Lancelet):
    support = "skeleton"
    def __init__(self, name, feedding_type, water_type):
        super().__init__(name)
        self.feeding_type = feedding_type
        self.water_type = water_type
        self.hidden = False
    def hide(self, place):
        self.hidden =True
        print(f"{self.name.capitalize()} hides in  the {place}, in the {self.water_type} water")
    def reveal(self):
        self.hidden = False
        self.move("forward")
    def eat(self, subject):
        print(self, subject)
        print(f"{self.name.capitalize()} eats {subject}, since it is {self.feeding_type}")
        
if __name__ == "__main__":
    print(Clownfish.describe())
    clownfish = Clownfish(name="Amphiprion", feedding_type="omnivrous", water_type="salt")
    clownfish.move("left")
    clownfish.eat("zooplankton")
    clownfish.hide("anemone")
    clownfish.reveal()
    
    print(f"CLownfish is {'resting' if clownfish.hidden else 'swimming'}")