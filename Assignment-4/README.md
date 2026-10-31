# GenAI Python Assignment – Solution

## Overview

This repository contains solutions to Python programming exercises focused on file handling. The programs demonstrate creating and writing text files, reading file contents in different ways, appending data, counting lines, generating summary reports, collecting product information from the user, checking whether a file exists, and exporting discounted prices.

## Assignment Task-to-File Mapping

The mapping below is based on the functionality implemented in the submitted Python files. Match these descriptions to the task numbers in the assignment sheet if its numbering differs.

| Task / Program | File | What the program does | Main concepts |
|---|---|---|---|
| Write sales data to a file | `sales_record.py` | Writes a predefined list of sales values to `sales_data.txt` and reads the saved content. | Functions, `open()`, write mode (`"w"`), `write()`, `read()`, `join()` |
| Read file contents | `read_file.py` | Demonstrates reading the first line, reading all lines, and reading the entire file. It also converts the lines into integers. | `readline()`, `readlines()`, `read()`, `map()`, `int()` |
| Append new sales data | `new_sales.py` | Appends new sales values to `sales_data.txt`, reads the updated file, and counts its lines. | Append mode (`"a"`), `write()`, `read()`, `splitlines()`, `len()` |
| Generate sales summary report | `summary_report.py` | Reads sales values from `sales_data.txt`, converts them to integers, and displays total, highest, lowest, and average sales. | `readlines()`, `map()`, `int()`, `sum()`, `max()`, `min()`, `len()` |
| Create product information file | `product_info.py` | Accepts three product names and prices, writes them to `products.txt`, then reads and displays the saved records. | `input()`, lists, `append()`, `write()`, `readlines()`, `strip()`, `split()` |
| Read a file safely | `file_safty.py` | Asks for a filename, checks whether it exists, and either displays its contents or prints a file-not-found message. | `os.path.exists()`, `if-else`, `with open()`, `read()` |
| Export discounted prices | `discounted_price.py` | Calculates discounted prices for products, writes the results and summary information to `discount_report.txt`, and displays the report. | Dictionaries, `items()`, loops, arithmetic, `write()`, `read()`, `sum()`, `len()` |

## File Details

### 1. `sales_record.py`
- Stores sales values in a list.
- Converts the values into newline-separated text.
- Writes the content to `sales_data.txt`.
- Reads the file and prints its contents.

### 2. `read_file.py`
- Uses `readline()` to read only the first line.
- Uses `readlines()` to read all lines into a list.
- Converts the lines into integers using `map()` and `int()`.
- Uses `read()` to read the entire file as one string.

### 3. `new_sales.py`
- Stores additional sales values in a list.
- Converts the values into newline-separated text.
- Appends the new values to `sales_data.txt`.
- Reads the updated file and counts the number of lines.

### 4. `summary_report.py`
- Reads sales values from `sales_data.txt`.
- Converts the text values into integers.
- Calculates and displays total sales, highest sale, lowest sale, and average sale.

### 5. `product_info.py`
- Asks the user to enter three product names and prices.
- Stores the entered products in a list.
- Writes product names and prices to `products.txt`.
- Reads the file and displays each product with its price.

### 6. `file_safty.py`
- Asks the user to enter a filename.
- Uses `os.path.exists()` to check whether the file exists.
- Reads and displays the file if it exists.
- Displays a message if the file cannot be found.

### 7. `discounted_price.py`
- Stores product names and original prices in a dictionary.
- Asks the user for a discount percentage.
- Calculates the discounted price of each product.
- Writes product name, original price, and discounted price to `discount_report.txt`.
- Adds the total number of products and average discounted price to the report.
- Reads and displays the generated report.

## Requirements

- Python 3.9 or later
- No third-party Python libraries are required.

## How to Run

1. Install Python if it is not already installed.
2. Download or clone this repository.
3. Extract the ZIP file if necessary.
4. Open a terminal in the project directory.
5. Run the required Python file using:

```bash
python filename.py
```

For example:

```bash
python sales_record.py
python read_file.py
python new_sales.py
python summary_report.py
python product_info.py
python file_safty.py
python discounted_price.py
```

Run each file independently. Some programs request input in the terminal, while others use predefined sample data. Run `sales_record.py` before `read_file.py` or `summary_report.py` if you want to recreate the initial sales data.

## Concepts Demonstrated

- Opening files using `open()`
- File modes: read (`"r"`), write (`"w"`), and append (`"a"`)
- Using `with open()` to manage files
- Reading with `read()`, `readline()`, and `readlines()`
- Writing content with `write()`
- Converting values using `str()` and `int()`
- Using `map()` to convert file lines into integers
- Using `join()` to combine values with newline characters
- Processing text with `strip()` and `split()`
- Counting lines using `splitlines()` and `len()`
- Lists, dictionaries, loops, and functions
- Basic calculations using `sum()`, `max()`, and `min()`
- Checking file existence with `os.path.exists()`

## Notes

- The filenames are preserved as provided in the submitted solution, including the spelling `file_safty.py`.
- The programs use relative filenames, so run them from the project directory.
- Write mode (`"w"`) replaces the existing file content.
- Append mode (`"a"`) adds content to the end of an existing file.
- Running `sales_record.py` recreates `sales_data.txt` with the five sample sales values.
- Running `new_sales.py` appends its three sample sales values. Running it multiple times adds those values again.
- `product_info.py` replaces the existing contents of `products.txt` each time it runs.
- `discounted_price.py` replaces the existing contents of `discount_report.txt` each time it runs.
