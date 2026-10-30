orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_orders = 0

print("Order Amount    | Discount       | Final Amount")

for order_amount in orders:

    if order_amount >= 2000:
        discount = 15
    elif order_amount >= 1500:
        discount = 10
    elif order_amount >= 1000:
        discount = 7
    else:
        discount = 0

    discount_amount = order_amount * discount / 100
    final_amount = order_amount - discount_amount

    print(order_amount, "\t\t|", discount, "%\t\t |", final_amount)
    total_revenue = total_revenue + final_amount

    if discount > 0:
        discounted_orders = discounted_orders + 1

print("Total Revenue:", total_revenue)
print("Orders receiving discount:", discounted_orders)