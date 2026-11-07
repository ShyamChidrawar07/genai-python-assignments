import streamlit as st

st.title("Simple Sales Dashboard")
st.write("This is a simple mini dashboard displaying monthly sales data.")

months = ["January", "February", "March", "April"]
selected_month = st.selectbox("Select a month:", months)

sales = {"January": 1200, "February": 1500, "March": 900, "April": 2000}
st.metric(label=f"Sales for {selected_month}", value=sales[selected_month])

st.subheader("Monthly Sales Chart")
st.bar_chart(list(sales.values()))
