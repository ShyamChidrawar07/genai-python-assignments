
from store import Store


def display_menu():
    print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Show All Products")
    print("4. Search Product")
    print("5. Calculate Total Inventory Value")
    print("6. Apply Product Discount")
    print("7. Show Store Summary")
    print("8. Exit")
    print("==================================================")


def main():

    store = Store("Shyam Electronics")
    inventory = store.inventory

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        # 1. Add Product
        if choice == "1":
            store.add_new_product()

        # 2. Remove Product
        elif choice == "2":
            name = input("Enter product name to remove: ")
            inventory.remove_product(name)

        # 3. Show All Products
        elif choice == "3":
            print("\n========== ALL PRODUCTS ==========")
            inventory.show_all_products()

        # 4. Search Product
        elif choice == "4":
            name = input("Enter product name to search: ")
            found = False
            for product in inventory.products:
                if product.name.lower() == name.lower():
                    print("\nProduct Found:")
                    product.get_info()
                    found = True
                    break
            if not found:
                print(f"Product '{name}' not found.")

        # 5. Calculate Total Inventory Value
        elif choice == "5":
            total = inventory.get_total_value()
            print(f"Total Inventory Value: ₹{total}")

        # 6. Apply Product Discount
        elif choice == "6":
            name = input("Enter product name: ")
            for product in inventory.products:
                if product.name.lower() == name.lower():
                    try:
                        discount = float(input("Enter discount percentage: "))
                        discounted_price = product.apply_discount(discount)
                        print(f"Discounted Price: ₹{discounted_price} "f"after {discount}% discount on {product.name}")
                    except ValueError as error:
                        print(f"Invalid discount: {error}")
                    break
            else:
                print(f"Product '{name}' not found.")

        # 7. Show Store Summary
        elif choice == "7":
            store.show_summary()

        # 8. Exit
        elif choice == "8":
            print("\nThank you for using Inventory Management System!")
            break

        else:
            print("Invalid choice! Please select between 1 and 8.")

if __name__ == "__main__":
    main()
