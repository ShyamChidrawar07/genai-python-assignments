# GenAI Python Assignment – Modules and Packages

## Overview

This assignment demonstrates how to create and use **Python modules and packages** to organize reusable functions. The solution separates mathematical operations, string operations, billing calculations, and discount calculations into individual Python files, then imports and uses them in `main.py`.

## Assignment Task-to-File Mapping

| Task | File / Package | What the program does | Main concepts |
|---|---|---|---|
| Task 1: Create a simple module | `math_utils.py` | Defines `add()`, `subtract()`, and `square()` functions. Demonstrates importing the module and importing one function directly. | Modules, functions, `import`, `from ... import` |
| Task 2: Create another module | `string_utils.py` | Defines functions to capitalize each word, reverse a string, and count words. | String methods, slicing, `split()`, `len()` |
| Task 3: Create a package | `shop_package/` | Contains `billing.py`, `discount.py`, and `__init__.py` to organize shopping-related functions. | Packages, submodules, package initialization |
| Task 4: Import the package in `main.py` | `main.py` | Imports the discount module with an alias, imports billing functions, and calls them to calculate discounts, totals, and tax. | Package imports, aliases, function calls |

## Project Structure

```text
GenAI-Assignment(5)-ShyamChidrawar/
└── modules_assignment/
    ├── main.py
    ├── math_utils.py
    ├── string_utils.py
    └── shop_package/
        ├── __init__.py
        ├── billing.py
        └── discount.py
```

## File Details

### 1. `math_utils.py`

Creates a simple module containing three mathematical functions:

- `add(a, b)` – returns the sum of two numbers.
- `subtract(a, b)` – returns the difference between two numbers.
- `square(n)` – returns the square of a number.

The functions are used in `main.py` in two ways:

```python
import math_utils
from math_utils import square

math_utils.add(25, 15)
math_utils.subtract(25, 15)
square(10)
```

### 2. `string_utils.py`

Creates a module containing three string utility functions:

- `capitalize_words(text)` – returns the text with each word capitalized using `title()`.
- `reverse_string(text)` – returns the reversed string using slicing.
- `word_count(text)` – returns the number of words using `split()` and `len()`.

The module is imported in `main.py` using:

```python
import string_utils
```

### 3. `shop_package/`

Creates a Python package named `shop_package` with the following files:

#### `discount.py`

Contains two discount functions:

1. `apply_discount(price, percent)` – calculates the price after applying a percentage discount. It prints a message if the price is negative and returns the original price when the percentage is zero.
2. `flat_discount(price)` – subtracts a flat amount of ₹50 from a positive price. It prints a message if the price is zero or negative.

#### `billing.py`

Contains two billing functions:

1. `calculate_total(prices)` – calculates the sum of positive values in the supplied price list. Non-positive values are ignored.
2. `apply_tax(amount)` – adds 5% tax to a positive amount. It prints a message if the amount is zero or negative.

#### `__init__.py`

Initializes the `shop_package` package. It is left empty apart from the provided comment.

### 4. `main.py`

The main program imports and demonstrates the functions from the modules and package.

Imports used:

```python
from math_utils import square
import math_utils
import string_utils
from shop_package import discount as disc
from shop_package.billing import calculate_total, apply_tax
```

- `square` is imported directly from `math_utils`.
- `math_utils` is imported as a complete module and its functions are accessed using dot notation.
- `string_utils` is imported as a module.
- `discount` is imported from `shop_package` with the alias `disc`.
- `calculate_total` and `apply_tax` are imported directly from the `billing` submodule.

The program then demonstrates mathematical operations, string operations, percentage and flat discounts, billing total calculation, and 5% tax calculation.

## Requirements

- Python 3.9 or later
- No third-party Python libraries are required.

## How to Run

1. Install Python if it is not already installed.
2. Download or extract the assignment project.
3. Open a terminal in the `modules_assignment` directory (the directory containing `main.py`).
4. Run the main program:

```bash
python main.py
```

### Windows example

```bat
cd path\to\GenAI-Assignment(5)-ShyamChidrawar\modules_assignment
python main.py
```

No dependency installation or virtual environment is required for this assignment.

> **Important:** Keep `math_utils.py`, `string_utils.py`, and the `shop_package` folder at the same level as `main.py`. Run `main.py` from the `modules_assignment` directory so Python can locate the local modules and package.

## Expected Output

With the sample values currently defined in `main.py`, the output is:

```text
Square of 10 =  100
Addition of 25 & 15 is  40
Subtraction of 25 & 15 is  10
String for below demo is This is module and packages assignment
Capitalie every word in string. strs= This Is Module And Packages Assignment
String Reversed = tnemngissa segakcap dna eludom si sihT
Number of words in string = 6
Apply Discount of 10% on 1000= 900.0
Flat discount of RS.50 on 1000=  950
Total of prices [1000, 10, -10] = 1010
5% Tax on 1010 =  1060.5
```

## Concepts Demonstrated

- Creating and importing Python modules
- Creating a package using a directory and `__init__.py`
- Importing an entire module with `import`
- Importing selected functions with `from ... import`
- Importing a package submodule
- Using aliases with `as`
- Accessing module functions using dot notation
- Defining reusable functions
- Type hints and return values
- String methods and slicing
- Lists and loops
- Basic arithmetic and percentage calculations
- Conditional statements for basic input checks

## Notes

- The package directory must be named `shop_package` and must be located beside `main.py`.
- `__init__.py` is included inside `shop_package` to identify and initialize the package.
- The current `calculate_total()` implementation ignores zero and negative values. For an empty list, it prints `List is Empty` and returns `None`.
- The current `apply_tax()` implementation adds 5% to positive amounts and prints a message for non-positive amounts.
- `apply_discount()` checks for negative prices and handles a zero discount, but does not validate whether the percentage is between 0 and 100.
- `flat_discount()` subtracts ₹50 from a positive price; it does not prevent the final price from becoming negative if the original price is below ₹50.
- The `main.py` program uses predefined sample values and does not request user input.
