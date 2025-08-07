from random import randint


class Product():
    def __init__(self, name:str)-> None:
        self.name = name
        self._price = 0
        self.__sku = randint(1, 100)
    def set_price(self, price: float)->None:
        self._price = price
    def get_price(self):
        return self._price
    def get_sku(self):
        return self.__sku
    def get_details(self):
        return(f"Product name: {self.name}, product price {self.get_price()}, product unique number {self.get_sku()}")
    



if __name__ == '__main__':
    
    bread = Product("bread")
    bread.set_price(2.5)
    print(bread.get_price())
    print(bread.get_sku())
    print(bread.get_details())