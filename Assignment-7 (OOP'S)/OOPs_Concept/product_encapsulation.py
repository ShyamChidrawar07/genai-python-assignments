class Product:
    def __init__(self: object, name: str, price: int, category: str) -> None:
        self.name = name
        self.__price = price
        self.category = category

    def get_price(self: object) -> int:
        return self.__price

    def set_price(self: object, price: int) -> str:
        if price > 0:
            self.__price = price
        return f"Price updated to {self.__price}"

if __name__=="__main__":
    p=Product("Galaxy S25",80000,"Smartphones")
    price = p.get_price()
    print("Original Price",price)
    print("Update price to 86000")
    print(p.set_price(86000))
