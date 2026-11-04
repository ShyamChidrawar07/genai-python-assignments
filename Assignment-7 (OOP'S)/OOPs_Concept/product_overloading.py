from product import Product

class ProductOverloading(Product):
    def __init__(self: object, name: str, price: int, category: str) -> None:
        super().__init__(name, price, category)

    def __str__(self:object):
        return f"Product ({self.name},{self.price},{self.category})"
    
    def __add__(self:object, other:object) ->int :
        if isinstance(other, ProductOverloading) :
            return self.price + other.price

product1=ProductOverloading("Galaxy S25",80000,"Smartphones")
product2=ProductOverloading("Iphone 15",99000,"Smartphones")
print(product1)
print(product2)
total_price = product1 + product2
print("Total Price : ", total_price)