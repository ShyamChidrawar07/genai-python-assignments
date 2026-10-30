prices=[100,250,400,1200,50]
prices_with_gst = list(map(lambda price: price + (price * 0.18), prices))
print("Prices befor applying GST ", prices)
print("Prices after applying GST ", prices_with_gst)