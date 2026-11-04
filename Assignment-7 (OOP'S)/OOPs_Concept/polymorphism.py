from product import Product

class Laptop(Product):

    def get_info(self):
        print(f"Laptop: {self.name}")
        print(f"Price: {self.price}")
        print("Type: Laptop")

class Mobile(Product):

    def get_info(self):
        print(f"Mobile: {self.name}")
        print(f"Price: {self.price}")
        print("Type: Smartphone")

if __name__=="__main__":
    laptop = Laptop("Dell Inspiron", 55000, "Electronics")
    mobile = Mobile("Samsung S25", 75000, "Electronics")

    products = [laptop, mobile]
    for product in products:
        product.get_info()
        print()