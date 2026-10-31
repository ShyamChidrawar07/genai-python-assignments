def write_products(filename: str, products: list) -> None:
    with open(filename, "w") as f:
        for product in products:
            f.write(f"{product[0]} | {product[1]}\n")


def read_products(filename: str) -> None:
    with open(filename, "r") as f:
        lines = f.readlines()

        print("\nProduct Information")
        print("-------------------")

        for line in lines:
            product = line.strip().split("|")
            print(f"Product: {product[0]:15} Price: {product[1]}")


products = []

for i in range(3):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))

    products.append([name, price])


filename = "products.txt"

write_products(filename, products)
read_products(filename)
