from typing import List
#Введення в ООП, огляд класів
#Всі предмети->літаючі предмети->літаки->об'єднані кілкьістю двигунів->Boeing 777
class Plane():
    engine_type = "turbofan"
    def __init__(self, side_text:str,
                 main_color:str, additional_colors:List[str],
                 side_doors_count:int, autopilot:bool):

        self.side_text = side_text
        self.main_color = main_color
        self.additional_colors = additional_colors
        self.side_doors_count = side_doors_count
        self.autopilot = autopilot
#Це інстанс метод класу Plane, він приймає в аргументи (лише) свій інстанс
    def take_off(self):
        print(f"{self.side_text} takes off")
    def land(self):
        print(f"{self.side_text} lands")
#Це класовий метод
    @classmethod
    def inspect_engine(cls):   
        print(f"Plane has{cls.engine_type}")
    @staticmethod
    def calculate_fuel(distance:int):
        hour_fuel = 7000
        hour_distance = 900
        fuel = (hour_fuel * distance)/hour_distance
        print(f"For {distance} km plane needs {round(fuel)} kg of fuel")


boeing = Plane("Boeing", "Blue", ["red", "white", "green"], 5, True)
airbus = Plane("Airbus", "Green", ["blue", "dark"], 4, False)
print(boeing.side_text)
print(airbus.additional_colors)
boeing.take_off()
boeing.land()
airbus.take_off()
airbus.land()
print(f"Checking engine type{airbus.engine_type}")
print(Plane.calculate_fuel(1000),  boeing.calculate_fuel(3500),airbus.calculate_fuel(5300))


