# GenAI Python Assignment – Solution


## Overview

This repository contains solutions to Python programming exercises covering functions, recursion, lambda expressions, higher-order functions (`map()` and `filter()`), basic price calculations, and a menu-driven program.

## Assignment Task-to-File Mapping

The original assignment prompt was not available for direct verification while preparing this README. The mapping below is therefore based on the functionality implemented in the submitted Python files. Match these descriptions to the task numbers in the assignment sheet before submission if its numbering differs.

| Task / Program | File | What the program does | Main concepts |
|---|---|---|---|
| Factorial using a function | `funtion_utlity.py` | Defines a recursive `factorial()` function, accepts a number from the user, and displays its factorial. | Functions, recursion, conditional statements, user input |
| Apply GST to a single price | `gst_calculator.py` | Uses a lambda function to calculate a price after adding 18% GST. | Lambda expression, arithmetic |
| Apply GST to a list of prices | `map_function.py` | Uses `map()` with a lambda expression to add 18% GST to every price in a list. | Lists, `map()`, lambda |
| Filter products by price | `filter_products.py` | Splits a list of prices into values greater than 500 and values less than or equal to 500. | Lists, `filter()`, lambda |
| Price management menu | `menu.py` | Provides options to add prices, calculate their average, display the highest price, and quit. | Functions, lists, loops, conditionals, menu-driven programming |
| Calculate price after discount | `price_after_discount.py` | Defines `apply_discount()` with a default discount of 5%, checks input types, and prevents discounts above 60%. | Functions, default arguments, validation, conditionals |
| Combine discount and filtering operations | `combined_utility_function.py` | Applies a 10% discount to a list of prices and filters the discounted prices to retain values greater than 300. | Functions, `map()`, `filter()`, lambda, lists |

## File Details

### 1. `funtion_utlity.py`
- Takes an integer from the user.
- Calculates factorial recursively.
- Displays the factorial for valid non-negative inputs.

### 2. `gst_calculator.py`
- Accepts a product price.
- Calculates 18% GST using a lambda expression.
- Prints the final price including GST.

### 3. `map_function.py`
- Starts with a list of product prices.
- Uses `map()` to add 18% GST to each price.
- Displays the original and updated lists.

### 4. `filter_products.py`
- Uses `filter()` to separate prices greater than 500.
- Displays prices less than or equal to 500 separately.

### 5. `menu.py`
- Allows users to add multiple prices.
- Calculates the average of the stored prices.
- Displays the highest price.
- Continues until the user selects `q`.

### 6. `price_after_discount.py`
- Defines a reusable discount function.
- Uses 5% as the default discount.
- Rejects discounts above 60% and invalid input types.
- Includes example function calls.

### 7. `combined_utility_function.py`
- Applies a 10% discount to each price using `map()`.
- Uses `filter()` to select discounted prices greater than 300.
- Returns and displays both lists.

## Requirements

- Python 3.x
- No third-party libraries are required.

## How to Run

1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run the required file using:

```bash
python filename.py
```

For example:

```bash
python gst_calculator.py
python map_function.py
python filter_products.py
python menu.py
python funtion_utlity.py
python price_after_discount.py
python combined_utility_function.py
```

Run each file independently. Some programs request input in the terminal, while others use predefined example data.

## Concepts Demonstrated

- Defining and calling functions
- Recursive functions
- Default function arguments
- Basic input validation
- Lambda expressions
- `map()` for transforming list elements
- `filter()` for selecting list elements
- Lists and built-in operations such as `sum()` and `max()`
- Loops and conditional statements
- Menu-driven command-line programs

## Notes

- The filenames are preserved as provided in the submitted solution.
- `funtion_utlity.py` contains the original spelling of the submitted filename.
- The task descriptions above summarize the current implementation; they are not a substitute for the exact wording of the assignment questions.
