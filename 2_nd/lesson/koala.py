from lancelet import Lancelet

class Koala(Lancelet):
    habitation = "forest"
    support = "skeleton"
    def __init__(self, name, sleepping=False):
        super().__init__(name)
        self.sleeping =  sleepping
    def eat(self, subject):
        if not self.sleeping:
            self.move("up")
            print(f"{self.name.capitalize()} climbs to tree to eat {subject}")
        else: 
            print(f"{self.name.capitalize()} cannot eat while sleepibg")
    def change_state(self):
        if self.sleeping: 
            print(f"{self.name.capitalize()} is waking up")
        else: 
            print(f"{self.name.capitalize()} lies on a branch and sleeps")
        self.sleeping = not self.sleeping


if __name__ == '__main__':
    print(Koala.describe())
    koala = Koala(name="Phascolarctos")
    koala.move("right")
    koala.eat("eucalyptus leaves")
    koala.change_state()
    koala.eat("eucalyptus leaves")
    koala.change_state()