from product import Product
from inventory import Inventory


class Store:
    def __init__(self, store_name: str):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self) -> None:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        category = input("Enter product category: ")
        product = Product(name, price, category)
        self.inventory.add_product(product)

    def show_summary(self) -> None:
        total_items = len(self.inventory.products)
        total_value = self.inventory.get_total_value()

        print("\n========== STORE SUMMARY ==========")
        print(f"Store Name       : {self.store_name}")
        print(f"Total Items      : {total_items}")
        print(f"Total Inventory Value : {total_value}")
        print("====================================")

if __name__ == "__main__":
    # 1. Create Store object
    store = Store("Shyam Electronics")

    # 2. Add three products
    store.add_new_product()
    store.add_new_product()
    store.add_new_product()

    print("\n========== ALL PRODUCTS ==========")
    store.inventory.show_all_products()
    store.show_summary()

    # Test __add__() using first two products
    products = store.inventory.products

    if len(products) >= 2:
        total_price = products[0] + products[1]
        print(f"\nCombined Price of First Two Products: {total_price}")