order_amounts = []

while True:
    print("\n\t\tUser Menu")
    print("\t\t1. Add Order Amount")
    print("\t\t2. Show Orders & Totals")
    print("\t\tq. Quit\n")

    choice = input("Select an option - ")

    if choice == "1":
        order_amount = int(input("Enter Order Amount - "))
        order_amounts.append(order_amount)


    elif choice == "2":
        print("Orders and Totals")
        print("Order Amount List", order_amounts)
        total_revenue = 0
        discounted_orders = 0
        print("order_amount | discount%| final_amount")

        for order_amount in order_amounts:
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
            print(f"\t{order_amount} |\t{discount}\t| {final_amount}")

            total_revenue = total_revenue + final_amount

        print("Total Revenue:", total_revenue)

    elif choice == "q":
        break

    else:
        print("Enter Valid Choice")
        continue
