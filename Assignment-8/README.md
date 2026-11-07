# Streamlit Python Assignment – Mini Applications

## Overview

This assignment demonstrates how to build basic interactive web applications using Python and Streamlit. It contains four mini applications covering text input, button interactions, price calculations, sidebar forms, input validation, metrics, and charts.

## Assignment Task-to-File Mapping

| Task | File | What the program does | Main concepts |
|---|---|---|---|
| Task 1: Basic Streamlit app | `app_basic.py` | Displays a welcome title, accepts the user's name, and displays a greeting when the button is clicked. | `st.title()`, `st.text_input()`, `st.button()`, `st.write()`, class and method |
| Task 2: Price calculator | `app_discount.py` | Accepts an original price and discount percentage, then calculates and displays the discounted price. | `st.number_input()`, `st.button()`, arithmetic operations, class method |
| Task 3: Product form | `app_product_form.py` | Collects product name, price, category, and quantity through a sidebar form, validates the inputs, and creates a product object. | `st.sidebar.form()`, `st.text_input()`, `st.number_input()`, `st.selectbox()`, form submission, validation, class and object |
| Task 4: Mini dashboard | `app_dashboard.py` | Lets the user select a month, displays its sales value, and presents monthly sales in a bar chart. | `st.selectbox()`, dictionary, `st.metric()`, `st.bar_chart()` |

## Project Structure

```text
streamlit_assignment/
├── app_basic.py
├── app_discount.py
├── app_product_form.py
├── app_dashboard.py
└── README.md
```

## File Details

### 1. `app_basic.py`

Defines an `Introduction` class with an `intro()` method that displays a simple welcome application.

- Displays the title `Welcome to Streamlit!` using `st.title()`.
- Accepts the user's name using `st.text_input()`.
- Displays a **Greet Me** button using `st.button()`.
- When the button is clicked, displays a greeting containing the entered name using `st.write()`.

**Main components used:**

- `st.title()`
- `st.text_input()`
- `st.button()`
- `st.write()`

**Implementation note:** The `intro()` method is defined without `self` and is called through the class. The program works in this usage, although declaring it as a `@staticmethod` would make the intended method behavior clearer.

### 2. `app_discount.py`

Defines a `Discount` class with methods to calculate the discounted price and collect user input through Streamlit.

- `apply_discount(price, discount_percentage)` calculates the final price after applying the discount.
- Accepts the original price using `st.number_input()` with a minimum value of 1.
- Accepts the discount percentage using `st.number_input()` with a range from 1 to 100.
- Displays a **Calculate Discount** button.
- When clicked, calculates and displays the discounted price.

**Calculation**

```text
Discount Amount = Original Price × (Discount Percentage / 100)
Final Price     = Original Price - Discount Amount
```

**Example**

| Description | Amount |
|---|---:|
| Original price | 1000 |
| Discount | 10% |
| Discount amount | 100 |
| Final price | 900 |

**Implementation note:** The assignment screenshot describes a slider with a 0–50% range. The current implementation uses a number input with a 1–100% range. The file also calculates a sample discounted price of `900.0` and prints it in the terminal when the script runs.

### 3. `app_product_form.py`

Defines a `Product` class to store product details and collect them through a Streamlit sidebar form.

The form accepts the following information:

- Product name
- Product price
- Product category
- Product quantity

**Available categories**

- Electronics
- Clothing
- Books
- Groceries
- Other

**Form behavior**

1. Displays the product form in the sidebar using `st.sidebar.form()`.
2. Accepts the product name using `st.text_input()`.
3. Accepts the price using `st.number_input()`.
4. Provides category choices using `st.selectbox()`.
5. Accepts the quantity using `st.number_input()`.
6. Submits the form using `st.form_submit_button("Add Product")`.
7. Checks that the product name is not empty.
8. Checks that the price is greater than zero.
9. Creates a `Product` object when the validation checks pass.
10. Displays a success message in the sidebar.

The `Product` class stores the submitted name, price, category, and quantity as object attributes.

**Main components used:**

- `st.sidebar.form()`
- `st.text_input()`
- `st.number_input()`
- `st.selectbox()`
- `st.form_submit_button()`
- `st.sidebar.error()`
- `st.sidebar.success()`

**Implementation note:** The form is configured with `clear_on_submit=True`. The created product object is returned by `Product.get_input()` and its data is printed in the terminal. The current form does not display the full product details in the main Streamlit page.

### 4. `app_dashboard.py`

Creates a simple sales dashboard using predefined monthly sales data.

- Displays the title `Simple Sales Dashboard`.
- Displays a short description of the dashboard.
- Provides a month selector with January, February, March, and April.
- Stores the monthly sales values in a dictionary.
- Displays the selected month's sales using `st.metric()`.
- Displays a monthly sales bar chart using `st.bar_chart()`.

**Sample sales data**

| Month | Sales |
|---|---:|
| January | 1200 |
| February | 1500 |
| March | 900 |
| April | 2000 |

**Main components used:**

- `st.title()`
- `st.write()`
- `st.selectbox()`
- `st.metric()`
- `st.subheader()`
- `st.bar_chart()`

**Implementation note:** The chart is currently created from `list(sales.values())`, so it receives the sales values without explicit month labels as its index.

## Requirements

- Python 3.9 or later
- Streamlit
- No database or external API is required.

## How to Run

1. Install Python if it is not already installed.
2. Download or extract the assignment files.
3. Open a terminal in the project directory.
4. Install Streamlit:

```bash
pip install streamlit
```

5. Run the required application using the `streamlit run` command.

For example:

```bash
streamlit run app_basic.py
```

Other applications can be run individually:

```bash
streamlit run app_discount.py
streamlit run app_product_form.py
streamlit run app_dashboard.py
```

### Windows example

```bat
cd path\to\streamlit_assignment
streamlit run app_dashboard.py
```

Streamlit starts a local development server. Open the URL displayed in the terminal, usually:

```text
http://localhost:8501
```

Stop the running application with `Ctrl + C` in the terminal.

## Expected Output

The displayed output depends on the application and the values entered by the user.

Examples of the program behavior:

- `app_basic.py` displays a welcome title and shows a personalized greeting after the user enters a name and clicks **Greet Me**.
- `app_discount.py` displays the calculated discounted price after the user enters a price and discount percentage and clicks **Calculate Discount**. For an original price of `1000` and a discount of `10%`, the final price is `900.0`.
- `app_product_form.py` displays validation errors for an empty product name or a price that is not greater than zero. For valid details, it displays a success message and captures the product object.
- `app_dashboard.py` displays the selected month's sales value and a bar chart containing the sales values for all four months.

## Concepts Demonstrated

- Creating interactive web applications with Streamlit
- Displaying titles, text, and messages
- Collecting user input with text and number inputs
- Handling button clicks
- Creating and submitting sidebar forms
- Using select boxes to provide choices
- Validating user input
- Defining Python classes and methods
- Creating objects and storing object attributes
- Performing percentage-based calculations
- Using dictionaries to store related data
- Displaying key values with `st.metric()`
- Creating bar charts with `st.bar_chart()`

## Notes

- Each `.py` file is a separate Streamlit application and should be run individually.
- Use `streamlit run filename.py` to launch an application; running it with `python filename.py` will not start the Streamlit web interface as intended.
- `app_discount.py` currently uses number inputs rather than the slider shown in the assignment instructions.
- `app_discount.py` accepts discount percentages from 1 to 100, while the assignment screenshot specifies a range from 0 to 50%.
- `app_product_form.py` creates a product object and prints its details in the terminal; it does not save product data to a database.
- `app_dashboard.py` uses predefined sample data rather than data from an external source.
- The applications use Streamlit and Python; no additional libraries are needed beyond Streamlit.

