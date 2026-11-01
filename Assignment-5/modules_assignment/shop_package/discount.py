def apply_discount(price: float,percent: int) -> float:
    if price < 0:
        print("Price cannot be negative")
    elif percent == 0:
        return price
    else:
        return price - (price * percent / 100)

def flat_discount(price:int)-> int:
    if price==0:
        print("Price cannot be 0")
    elif price<0:
        print("Price Can't be Negative")
    else:
        return price-50

if __name__=="__main__":
    print(apply_discount(1000,10))
    print(apply_discount(-1000,10))
    print(apply_discount(1000.0,0))

    print(flat_discount(1000))
    print(flat_discount(-1000))
    print(flat_discount(00))