cart = []
while True:
    user_input = input("Enter product price (or 'q' to quit): ")
    if user_input.lower() == "q":
        break

    try:
        price = float(user_input)
        if price < 0:
            raise Exception("Price cannot be negative!")

        cart.append(price)
        print(f"Price {price} added to cart.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

    except Exception as e:
        print(e)

# Display shopping cart summary
print("\n----- Shopping Cart Summary -----")

print("Total items:", len(cart))
print("Total bill:", sum(cart))
