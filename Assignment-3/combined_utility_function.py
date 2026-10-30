def process_pricess(prices:list) ->list :
    discounted_prices= list(map(lambda x:int(x-(x*0.10)),prices))
    filtered_prices= list(filter(lambda x:x>300,discounted_prices))
    return discounted_prices, filtered_prices

prices = [100,500,900,50,750]
discounted_prices, filtered_prices = process_pricess(prices)
print("Prices after 10% discount :",discounted_prices)
print("Discounted prices greater than 300 :",filtered_prices)