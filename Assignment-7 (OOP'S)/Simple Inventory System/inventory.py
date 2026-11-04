
from product import Product

class Inventory:
    def __init__(self: object) -> None:
        self.products = []

    def add_product(self: object, product):
        for existing_product in self.products:
            if existing_product.name == product.name:
                print(f"Product '{product.name}' already exists.")
                return
        self.products.append(product)
        print(f"Product '{product.name}' added successfully.")

    def remove_product(self: object, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Product '{name}' removed successfully.")
                return
        print(f"Product '{name}' does not exist.")

    def get_total_value(self: object) -> float:
        total_value = 0
        for product in self.products:
            total_value += product.price
        return total_value

    def show_all_products(self: object) -> None:
        for product in self.products:
            product.get_info()
            print()


if __name__ == "__main__":

    inventory = Inventory()
    product1 = Product("Galaxy S25", 80000, "Smartphones")
    product2 = Product("Iphone 15", 99000, "Smartphones")

    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product1)

    # Display products
    print("\nAll Products in Inventory:")
    inventory.show_all_products()

    # Total inventory value
    print(f"Total Inventory Value: {inventory.get_total_value()}")

    # Removing product
    inventory.remove_product("Galaxy S25")
    print("\nAfter removing Galaxy S25:")
    inventory.show_all_products()
