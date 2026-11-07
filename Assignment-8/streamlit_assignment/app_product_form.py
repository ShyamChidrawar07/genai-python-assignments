import streamlit as st

class Product:
    def __init__(self, name: str, price: float, category: str, quantity: int):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity

    @staticmethod
    def get_input():
        # Setup form layout
        with st.sidebar.form("Product Details Form", clear_on_submit=True):
            product_name = st.text_input("Enter the product name:")
            price = st.number_input("Enter product price:", min_value=0.0, step=0.01, format="%.2f")
            categories = ["Electronics","Clothing","Books","Groceries","Other"]
            category = st.selectbox("Select product category:", options=categories)
            quantity = st.number_input("Enter product quantity:", min_value=0, step=1)

            submitted = st.form_submit_button("Add Product")
            if submitted:
                if not product_name.strip():
                    st.sidebar.error("Product name cannot be empty!")
                    return None
                if price <= 0:
                    st.sidebar.error("Price must be greater than zero!")
                    return None
                if quantity < 0:
                    st.sidebar.error("Quantity cannot be negative!")
                    return None

                new_product = Product(product_name, price, category, quantity)
                st.sidebar.success(f"'{product_name}' successfully added!")
                return new_product
        return None


if __name__ == "__main__":
    # Capture the product object returned from the static method
    product_data = Product.get_input()
    print(
        f"Captured Product Data: {product_data.__dict__}"
        if product_data
        else "No product data captured."
    )
