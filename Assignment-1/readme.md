# GenAI Assignment 1 – Python Data Structures

## Overview

This assignment demonstrates how Python data structures can be used to manage a simple product catalogue. The solutions cover lists, tuples, sets, and dictionaries, followed by combining these structures to organize products by category.

## Task-to-File Mapping

| Task | File | What the solution does | Main concepts |
|---|---|---|---|
| Task 1 – Product collections | `product_collections.py` | Reads product names using list indexing, accesses the last item, appends new products, converts a tuple to a list for editing, and converts it back to a tuple. | Lists, indexing, negative indexing, `append()`, tuples, type conversion |
| Task 2 – Product categories | `categories.py` | Creates a set from category names, demonstrates duplicate removal, adds categories, checks whether a category exists, and counts unique categories. | Sets, `add()`, `issubset()`, `len()` |
| Task 3 – Product pricing | `product_pricing.py` | Stores product prices in a dictionary, inserts a new product, removes a product using dictionary comprehension, and calculates the average of the remaining prices. | Dictionaries, keys and values, dictionary comprehension, `values()`, aggregation |
| Task 4 – Combined catalogue operations | `combined_operations.py` | Combines product names, prices, and categories into catalogue records; creates a category-to-products mapping; and identifies the category containing the most products. | Lists, tuples, dictionaries, list comprehension, dictionary comprehension, `max()` with `key` |

## Project Files

```text
GenAI-Assignment(1)-ShyamChidrawar/
├── categories.py
├── combined_operations.py
├── product_collections.py
├── product_pricing.py
└── README.md
```

## How to Run

1. Extract the ZIP archive.
2. Open a terminal in the extracted assignment folder.
3. Run any task independently:

```bash
python product_collections.py
python categories.py
python product_pricing.py
python combined_operations.py
```

On systems where the Python command is `python3`, use `python3` instead.

## Expected Output

Each file prints the result of its operations to the terminal:

- `product_collections.py` displays selected and updated product collections.
- `categories.py` displays the original and updated category set, membership check, and unique-category count.
- `product_pricing.py` displays dictionary updates and the average price after removal.
- `combined_operations.py` displays the catalogue, category-to-products mapping, and category with the highest product count.

The exact ordering of set elements may vary because sets are unordered.

## Notes

- Each task is implemented in a separate Python file for easy review and execution.
- The programs use sample product and price data directly in the source code.
- No external packages or database are required.
