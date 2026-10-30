def apply_discount(price,discount_percent=5):
    if type(price) == int and type(discount_percent) == int:
            if discount_percent == 0:
                return price
            if discount_percent >60:
                return "Discount can not exceed 60 percent"        
            else:
                discounted_price = price * (discount_percent / 100)
                final_price = price-discounted_price
                return f" Final Price = {final_price}"
    else:
        return "Enter Valid input type"
        
print(apply_discount(1000, 10))
print(apply_discount(500))
print(apply_discount(0))
print(apply_discount("s"))
print(apply_discount(True))