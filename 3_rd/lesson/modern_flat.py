from flat import Flat
class modern_flat(Flat):
    def __init__(self, number):
        super().__init__(number)
        self._room_number = 3
        self._design = "modern"
        self._has_tv = True
    def get_room_number(self, friend = False):
        return self._room_number if friend else 0 
    def get_design(self, friend = False):
        return self._design if friend else "undefined"
    def update_design(self, design, friend=False):
        if friend and design.startswith("modern"):
            self._design  = design
    def turn_of_tv(self, friend=False):
        if friend and self._has_tv:
            print("TV turned on")
        else: 
            print("Not defined")




if __name__ == "__main__":
    flat = modern_flat(212)
    print(flat.display_number())
    print(flat.get_design(friend=True))
    