products = [
    "Samsung Galaxy S21",
    "Asus Vivobook 15",
    "Redmi Pad 2",
    "Apple Smartwatch 11",
    "JBL Tune290",
    "Canon 245",
]
sample_products = ("Samsung Galaxy S21", 75000, "Mobile")


print(f"2nd Product: {products[1]} ")
print(f"Last Product: {products[-1]} ")

products.append("JbL Go")
products.append("Realme Charger")
print(f"Updated Products List: {products} ")

sample_products_list = list(sample_products)
print(f"Sample Products List: {sample_products_list} ")
sample_products_list[0] = ("Samsung Galaxy S22", 70000, "Mobile")
sample_products = tuple(sample_products_list)
print(f"Updated Sample Products: {sample_products} ")
