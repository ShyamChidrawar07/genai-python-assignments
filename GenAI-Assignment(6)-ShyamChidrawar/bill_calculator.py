prices = [120, 350, "abc", 500, -200, 800]
add = 0
for price in prices:
    try:
        if not isinstance(price, int):
            raise TypeError(f"Value {price} is not a Number")

        if price < 0:
            raise ValueError(f"Price cannot be negative: {price}")
        else:
            add += price
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        continue

print(f"Total Price: {add}")

