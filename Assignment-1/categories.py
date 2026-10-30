categories = ["Mobile", "Laptop", "Tablet", "Smartwatch", "Headphones", "Camera"]

print("Original Categories List:", categories) 
categories_set = set(categories)
print("\nSet ignore duplicate elements\n")
categories_set.add("Laptop")
print(categories_set)

categories_set.add("Bags")
print("\nUpdated Categories set",categories_set)

print("Check Category- Health is present ")
print( {"Health"}.issubset(categories_set))
print("Total No. of Unique Categories in Sets = ",len(categories_set))
