order_amount = input("Enter order amount: ")

if order_amount.isdigit():
    order_amount = int(order_amount)
    if order_amount >= 2000:
        discount= order_amount * 0.15
        discounted_price = order_amount - discount
        print("Final Amount after 15 percent discount ",discounted_price)
        tax =discounted_price * 0.05
        print(f"Subtotal = {discounted_price}, tax = {tax}, Final Total ={discounted_price+tax}")

        
    elif 1500 <= order_amount and order_amount < 2000:
        discount= order_amount * 0.10
        discounted_price = order_amount - discount
        print("Final Amount after 10 percent discount ",discounted_price)
        tax =discounted_price * 0.05
        print(f"Subtotal = {discounted_price}, tax = {tax}, Final Total ={discounted_price+tax}")
        
    elif 1000 <= order_amount and order_amount < 1500:
        discount= order_amount * 0.07
        discounted_price=order_amount - discount
        print("Final Amount after 7 percent discount ",discounted_price)
        tax = discounted_price * 0.05
        print(f"Subtotal = {discounted_price}, tax = {tax}, Final Total ={discounted_price + tax}")

    else:
        print("Final Amount ", order_amount)
    
else:
    print("Error: Please enter a valid integer.")
