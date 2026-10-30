products=["Mobile","Laptop", "Tablet","Smartwatch","Headphones","Camera"]
price_dict={
    "Samsung Galaxy S21": 78000,
    "Asus Vivobook 15" : 80000,
    "Redmi Pad 2" : 16000,
    "Apple Smartwatch 11" :35000,
    "JBL Tune290": 12000,
    "Canon 245":32000
}
print("Prodect to price dictonary",price_dict)
price_dict["Reame Bud2" ]= 3000
print("Prodect to price dictonary", price_dict)
price_dict = {key: val for key, val in price_dict.items() if key != "Redmi Pad 2"}
print(price_dict)
prices =price_dict.values()
dict_len=len(prices)
print(prices)
sum=sum(price for price in prices)
print("Average=", sum / dict_len)