from product import Product

class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years

    def get_info(self):
        super().get_info()
        print(f"Warranty: {self.warranty_years} years")

if __name__=="__main__":
    laptop = ElectronicProduct("HP Laptop", 60000, "Electronics", 2)
    laptop.get_info()
