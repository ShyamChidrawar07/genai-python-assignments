import streamlit as st


class Discount:
    def apply_discount(price: int, discount_percentage: int) -> float:
        discounted_price = price - (price * (discount_percentage / 100))
        return discounted_price

    def get_input():
        st.title("Discount Calculator")
        price = int(st.number_input("Enter the original price: ", min_value=1, step=1))

        discount_percentage = int(st.number_input("Enter the discount percentage: ", min_value=1, max_value=100, step=1))
        if st.button("Calculate Discount"):
            discounted_price = Discount.apply_discount(price, discount_percentage)
            st.write(f"The discounted price is: ${discounted_price}")

if __name__ == "__main__":
    Discount.get_input()
    discounted_price = Discount.apply_discount(1000,10)
    print(f"The discounted price is: ${discounted_price}" )

