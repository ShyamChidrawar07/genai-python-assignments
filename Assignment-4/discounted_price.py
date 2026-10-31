prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000,
}


def generate_report(filename: str, prices: dict, discount: float) -> None:

    discounted_prices = []

    with open(filename, "w") as f:
        f.write("Product | Original Price | Discounted Price\n")
        f.write("---------------------------------------------\n")

        for product, price in prices.items():
            discounted_price = price - (price * discount / 100)

            discounted_prices.append(discounted_price)

            f.write(f"{product} | {price} | {discounted_price:.2f}\n")

        total_items = len(prices)
        average_price = sum(discounted_prices) / total_items

        f.write("\nTotal Items: " + str(total_items))
        f.write("\nAverage Discounted Price: " + str(round(average_price, 2)))


def read_report(filename: str) -> None:
    with open(filename, "r") as f:
        print(f.read())


filename = "discount_report.txt"

discount = float(input("Enter discount percentage: "))

generate_report(filename, prices, discount)

print("\nDiscount Report")
print("----------------")

read_report(filename)
