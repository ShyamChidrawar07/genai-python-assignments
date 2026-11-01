from math_utils import square
import math_utils
import string_utils
from shop_package import discount as disc
from shop_package.billing import calculate_total,apply_tax

n, a, b =10, 25, 15
print(f"Square of {n} = ",square(n))
print(f"Addition of {a} & {b} is ", math_utils.add(a,b))
print(f"Subtraction of {a} & {b} is ", math_utils.subtract(a,b))

strs="This is module and packages assignment"
print(f"String for below demo is {strs}")
print("Capitalie every word in string. strs=",string_utils.capitalize_words(strs))
print("String Reversed =",string_utils.reverse_string(strs))
print("Number of words in string =",string_utils.word_count(strs))

price, percent = 1000, 10
print(f"Apply Discount of {percent}% on {price}=", disc.apply_discount(price,percent))
print(f"Flat discount of RS.50 on {price}= ",disc.flat_discount(price))

prices = [1000, 10, -10]
amount = calculate_total(prices)
print(f"Total of prices {prices} = {amount}")
print(f"5% Tax on {amount} = ",apply_tax(amount))