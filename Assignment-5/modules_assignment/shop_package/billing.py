def calculate_total(prices:list) -> int:
    if len(prices)==0:
        print("List is Empty")
    else:
        sum=0
        for price in prices:
            if price >0:
                sum=sum+price
        return sum
    

def apply_tax(amount:int)-> float:
    if amount<= 0:
        print("Enter Valid amount")
    else:
        return amount + (amount * 0.05)

if __name__ == "__main__":
    print(calculate_total([1000, 10, -10]))
    print(calculate_total([]))

    print(apply_tax(1000))
    print(apply_tax(-1000))