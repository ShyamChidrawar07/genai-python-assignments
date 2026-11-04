class Product:
    def __init__(self:object, name:str, price:int ,category: str) -> None:
        self.name=name
        self.price=price
        self.category=category
    
    def get_info(self:object)-> None:
        print("Product Name : ",self.name)
        print("Product Price : ",self.price)
        print("Product Category : ",self.category)

    def apply_discount(self:object, discount_percentage:int)-> None:
        discount_amount=(self.price*discount_percentage)/100
        self.price=self.price-discount_amount
        return f"Discounted Price : {self.price} after {discount_percentage}% discount on {self.name}"


if __name__=="__main__":
    product1=Product("Galaxy S25",80000,"Smartphones")
    product2=Product("Iphone 15",99000,"Smartphones")
    product1.get_info()
    product2.get_info()
    print(product1.apply_discount(10))
    print(product2.apply_discount(15))