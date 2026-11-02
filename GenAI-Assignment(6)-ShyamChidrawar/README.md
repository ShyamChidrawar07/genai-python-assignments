# GenAI Python Assignment – Exception Handling

## Overview

This assignment demonstrates how to handle runtime errors in Python using built-in exceptions, custom-raised exceptions, and `try`, `except`, `else`, and `finally` blocks. The programs cover age validation, bill calculation, file-reading permissions, safe division, and a safe shopping cart.

## Assignment Task-to-File Mapping

| Task | File | What the program does | Main concepts |
|---|---|---|---|
| Task 1: Age validator | `age_validator.py` | Accepts an age, checks the value using a validation function, and reports whether it is valid. | Functions, type hints, `try`, `except`, `ValueError` |
| Task 2: Bill calculator | `bill_calculator.py` | Iterates through a list of prices, skips invalid or negative values, and calculates the total of accepted prices. | Lists, loops, `isinstance()`, `TypeError`, `ValueError`, `continue` |
| Task 3: File reader | `file_reader.py`, `demo.txt` | Checks whether a file exists, allows the user named `shyam` to read its first three lines, and handles missing-file and permission errors. | File handling, `os.path.exists()`, `FileNotFoundError`, `PermissionError`, `finally` |
| Task 4: Safe division utility | `safe_division_utility.py` | Takes numerator and denominator inputs, performs division, and handles zero-division and invalid-input errors. | `ZeroDivisionError`, `ValueError`, `try`, `except`, `else`, `finally` |
| Task 5: Safe shopping cart | `safe_shopping_cart.py` | Accepts product prices until the user enters `q`, rejects invalid and negative prices, and displays the item count and total bill. | Lists, loops, `float()`, `ValueError`, `raise`, `sum()`, `len()` |

## Project Structure

```text
exception_handling_assignment/
├── age_validator.py
├── bill_calculator.py
├── demo.txt
├── file_reader.py
├── safe_division_utility.py
├── safe_shopping_cart.py
└── README.md
```

## File Details

### 1. `age_validator.py`

Defines the `check_age(age: int) -> bool` function and asks the user to enter an age.

- `check_age()` is intended to validate an age and return `True` when accepted.
- The function raises a `ValueError` with a message when its validation condition is met.
- The exception is caught inside the function, the error is printed, and the function returns `False`.
- The entered value is converted to an integer before the function is called.

**Implementation note:** The current condition is `if not age >= 1 and age <= 120`. Because of the use of `and`, this does not correctly reject every value outside the intended 1–120 range. Review the condition if the assignment requires complete range validation. Also, non-integer input is converted before `check_age()` is called, so that conversion error is not handled by the function.

### 2. `bill_calculator.py`

Processes a predefined list of prices and calculates the total of accepted values.

- Iterates through each value in `prices`.
- Uses `isinstance(price, int)` to check that each value is an integer.
- Raises `TypeError` when a value is not an integer.
- Raises `ValueError` when a price is negative.
- Catches either exception, prints the error, and uses `continue` to move to the next value.
- Adds valid non-negative integer prices to `add` and prints the final total.

**Note:** The current type check accepts integers only. A floating-point value such as `120.50` is treated as an invalid type.

### 3. `file_reader.py` and `demo.txt`

Demonstrates file existence checks and basic permission handling.

The `read_file(filename, user)` function:

1. Checks whether the requested file exists using `exists()` from `os.path`.
2. Raises `FileNotFoundError` if the file does not exist.
3. Allows the username `shyam` to open and read the file.
4. Reads and prints the first three lines using `readlines()[:3]`.
5. Raises `PermissionError` for other usernames.
6. Catches both file-related exceptions and prints an error message.
7. Uses `finally` to print `File Operation Attempted` whether the operation succeeds or fails.

`demo.txt` is the sample text file supplied for testing. It contains notes about exception handling and the `OSError` exception family.

**Run this program from the directory containing both `file_reader.py` and `demo.txt`, or enter the correct path to the text file.** The username check is a simple program condition; it is not operating-system file security.

### 4. `safe_division_utility.py`

Performs division using two values entered by the user.

- Reads the numerator and denominator and converts both to integers.
- Performs division with `/`.
- Handles `ZeroDivisionError` when the denominator is zero.
- Handles `ValueError` when the entered values cannot be converted to integers.
- Uses `else` to print the result only when no exception occurs.
- Uses `finally` to print `Operation completed` after the attempt.

### 5. `safe_shopping_cart.py`

Creates a shopping cart that stores product prices entered by the user.

- Starts with an empty list named `cart`.
- Repeatedly asks for a product price.
- Stops accepting input when the user enters `q` (uppercase or lowercase).
- Converts each entered price to a floating-point number using `float()`.
- Raises an exception if the price is negative.
- Appends valid prices to the cart and confirms that the price was added.
- Handles invalid numeric input with `ValueError`.
- Handles the negative-price exception and continues the loop.
- Prints the total number of items using `len(cart)` and the total bill using `sum(cart)`.

**Note:** The current program raises the base `Exception` class for a negative price rather than defining a separate custom exception class.

## Requirements

- Python 3.9 or later
- No third-party Python libraries are required.

## How to Run

1. Install Python if it is not already installed.
2. Download or extract the assignment files.
3. Open a terminal in the directory containing the Python files.
4. Run the required program using Python. For example:

```bash
python age_validator.py
```

Other programs can be run individually:

```bash
python bill_calculator.py
python file_reader.py
python safe_division_utility.py
python safe_shopping_cart.py
```

### Windows example

```bat
cd path\to\exception_handling_assignment
python safe_shopping_cart.py
```

No dependency installation or virtual environment is required.

> **Important:** Keep `demo.txt` in the same directory as `file_reader.py` when using the sample filename. Run the program from the assignment directory or provide the correct file path.

## Expected Output

The output depends on the values entered by the user and, for `bill_calculator.py` and `bill_calculator.py`, the values already defined in the source code.

Examples of the program behavior:

- `age_validator.py` prompts for an age and prints the Boolean result returned by `check_age()`.
- `bill_calculator.py` reports invalid types and negative prices, then prints the sum of accepted integer prices. With the supplied list `[120, 350, "abc", 500, -200, 800]`, the accepted values total `1770`.
- `file_reader.py` prints the first three lines of the requested file for username `shyam`; otherwise it prints a permission error. A missing file produces a file-not-found error.
- `safe_division_utility.py` prints the quotient for valid inputs, or an error for invalid input or division by zero.
- `safe_shopping_cart.py` displays the number of accepted prices and their sum after the user enters `q`.

## Concepts Demonstrated

- `try` and `except` blocks
- Handling built-in exceptions such as `ValueError`, `TypeError`, `ZeroDivisionError`, `FileNotFoundError`, and `PermissionError`
- Raising exceptions with `raise`
- Using `else` when no exception occurs
- Using `finally` for code that should run after an attempt
- Defining and calling functions
- Type hints
- Lists, loops, and conditional statements
- Type conversion with `int()` and `float()`
- File existence checks and reading text files
- `continue` and `break`
- Calculating totals with `sum()` and item counts with `len()`

## Notes

- Each `.py` file is a separate program and should be run individually.
- `demo.txt` is the sample file used by `file_reader.py`.
- `bill_calculator.py` accepts only integer values because it checks each value with `isinstance(price, int)`.
- `safe_shopping_cart.py` accepts decimal prices, but rejects negative values.
- `file_reader.py` reads at most the first three lines and permits only the exact username `shyam` after the input is converted to lowercase.
- The age validation condition in `age_validator.py` should be reviewed if the intended rule is to accept only ages from 1 through 120.
- The programs use Python's built-in exception handling and do not require external packages.
