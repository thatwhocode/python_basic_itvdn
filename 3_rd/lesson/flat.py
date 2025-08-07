class Flat(): 
    def __init__(self, number):
        self.number = number
        self.door_color = "brown"
        self.electricity_readings = 0
    def display_number(self):
        return(f"Number of flat is {self.number}")




if __name__ =="__main__":
    flat = Flat(222)
    flat.display_number()
    print(f"Number is {flat.number }, door color is {flat.door_color} electriciity reading is {flat.electricity_readings}")