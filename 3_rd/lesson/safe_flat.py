from modern_flat import modern_flat


class SafeFlat(modern_flat):
    def __init__(self, number):
        super().__init__(number)
        self.__has_safe = True
        self.__safe_content = ["Money", "Gold", "Silver"]
        self.__price = 1000000
    def describe(self, friend = False, owner = False):
        description =(
            f"Flat {self.number} has {self.door_color}"
            f"door color and {self.electricity_readings}"
            f"electricity count"
        )
        friend_description=(
            f"Flat has {self._design}"
            f"rooms count has {self._room_number}"
            f"The flat has {'' if self._has_tv else ' no '} TV\n"
        )
        owner_description = (
            f"The flat price is {self.__price} USD "
            f" The flat has {''if self.__has_safe else 'no'} safe"
            f"{', '.join(self.__safe_content) if self.__safe_content else 'empty'}"
        )
        if friend :
            description+= friend_description
        if owner:
            description+= owner_description
        
        print(description)
if __name__ == "__main__":
    flat = SafeFlat(202)
    #flat.describe(friend=True)
    flat.describe(owner=True)