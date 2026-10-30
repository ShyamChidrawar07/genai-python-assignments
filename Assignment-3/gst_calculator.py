price=int(input("enter price "))
gst=lambda price: price+(price*0.18)
print("Price after 18% GST",gst(price))