prices = [100, 250, 400, 1200, 50,2000,850]
greater_than_500=list(filter(lambda x:x>500,prices))
less_than_equalto_500 = list(filter(lambda x: x <= 500, prices))
# less_than_equalto_500 = list(filter(lambda x: x not in greater_than_500,prices))
print("Original List: ",prices)
print("Prices Greater than 500 : ",greater_than_500)
print("Prices Less than Equal to 500 : ",less_than_equalto_500)
