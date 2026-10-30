def add_price(prices_list, price):
    prices_list.append(price)
    return prices_list


def get_average_price(price_list):
    average = sum(price_list) / len(price_list)
    return average


def get_max_price(price_list):
    max_price = max(price_list)
    return max_price


# Initialize outside the while loop
price_list = []

while True:
    print("\n\t1. Add Price")
    print("\t2. Show Average Price")
    print("\t3. Show Highest Price")
    print("\tq. Quit")

    choice = input("Select Operation Choice: ")

    if choice == "1":
        n = int(input("Enter no of price values to be added:\n"))
        print("Enter values ")

        for _ in range(n):
            price = int(input())
            price_list = add_price(price_list, price)

        print("Price List:", price_list)

    elif choice == "2":
        if len(price_list) == 0:
            print("No prices available")
        else:
            average = get_average_price(price_list)
            print("Average Price:", average)

    elif choice == "3":
        if len(price_list) == 0:
            print("No prices available")
        else:
            highest = get_max_price(price_list)
            print("Highest Price:", highest)

    elif choice == "q":
        print("Exiting program...")
        break

    else:
        print("Invalid Choice. Select a suitable choice")
