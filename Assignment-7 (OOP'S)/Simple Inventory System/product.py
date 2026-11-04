class Product:
    def __init__(self, name: str, price: float, category: str) -> None:
        self.name = name
        self.price = price
        self.category = category

    def __str__(self) -> str:
        return f"Product ({self.name}, {self.price}, {self.category})"

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price + other.price
        return NotImplemented

    def get_info(self) -> None:
        print("Product Name:", self.name)
        print("Product Price:", self.price)
        print("Product Category:", self.category)

    def apply_discount(self, discount_percentage: float) -> float:
        if not 0 <= discount_percentage <= 100:
            raise ValueError("Discount must be between 0 and 100.")
        discount_amount = self.price * discount_percentage / 100
        return self.price - discount_amount


if __name__ == "__main__":
    product1 = Product("Galaxy S25", 80000, "Smartphones")
    product2 = Product("Iphone 15", 99000, "Smartphones")

    product1.get_info()
    product2.get_info()

    print(product1.apply_discount(10))
    print(product2.apply_discount(15))
    print("Total Price:", product1 + product2)
    print(product1)
