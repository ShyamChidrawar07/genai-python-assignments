products = [
    "Mobile",
    "Mobile",
    "Mobile",
    "Laptop",
    "Laptop",
    "Tablet",
    "Smartwatch",
    "Headphones",
    "Camera",
]
price_dict = {
    "Samsung Galaxy S21": 78000,
    "iPhone 17": 80000,
    "Redmi Note 14": 25000,
    "Asus Vivobook 15": 80000,
    "HP Pavilion": 65000,
    "Redmi Pad 2": 16000,
    "Apple Smartwatch 11": 35000,
    "JBL Tune290": 12000,
    "Canon 245": 32000,
}

catalog = [
    (list(price_dict.keys())[i], list(price_dict.values())[i], products[i])
    for i in range(len(products))
]

print("Catalog:")
print(catalog)

# 2. category-to-products mapping
category_to_products = {
    category: [name for name, price, cat in catalog if cat == category]
    for category in products
}

print("\n2. Category to Products:")
print(category_to_products)

# 3. Find the category with the maximum number of products 
max_category = max(category_to_products, key=category_to_products.get)

print("\n3. Products in the largest category:")
print(max_category, ":", category_to_products[max_category])