# GenAI Assignment 2 – Control Flow and Order Processing

## Overview

This assignment demonstrates Python control-flow concepts through order pricing and sales-processing examples. The programs apply conditional discount rules, calculate tax, process multiple orders, control loops, and provide a simple menu-driven interface.

## Task-to-File Mapping

| Task / Program | File | What the solution does | Main concepts |
|---|---|---|---|
| Single-order discount and tax calculation | `discount_rule.py` | Accepts an order amount, validates that the input contains digits, applies a discount based on the amount, calculates 5% tax on the discounted subtotal, and displays the final total. | `input()`, string validation with `isdigit()`, `if` / `elif` / `else`, arithmetic |
| Loop control in daily sales | `loop_control.py` | Processes daily sales values, skips days with zero sales, stops when corrupted data (`-1`) is encountered, and maintains a running total. | `for` loop, `break`, `continue`, accumulator |
| Processing multiple orders | `process_multiple_orders.py` | Applies discount slabs to a predefined list of orders, prints each order's discount and final amount, and calculates total revenue and the number of discounted orders. | Lists, loops, conditional statements, counters, accumulators |
| Menu-driven order management | `user_menu.py` | Repeatedly displays a menu that lets the user add order amounts, view orders and their discounted totals, or quit the program. | `while` loop, menu logic, `input()`, lists, `append()`, `break`, conditional statements |

## Discount Rules

The order-processing programs use these discount slabs:

| Order amount | Discount |
|---:|---:|
| ₹2,000 and above | 15% |
| ₹1,500 to ₹1,999 | 10% |
| ₹1,000 to ₹1,499 | 7% |
| Below ₹1,000 | 0% |

In `discount_rule.py`, an additional 5% tax is calculated on the discounted subtotal. The other order-processing scripts report discounted order amounts and revenue without adding tax.

## Project Files

```text
GenAI-Assignment(2)-ShyamChidrawar/
├── discount_rule.py
├── loop_control.py
├── process_multiple_orders.py
├── user_menu.py
├── tempCodeRunnerFile.py  # temporary editor-generated file; not an assignment task
└── README.md
```

`tempCodeRunnerFile.py` contains only a temporary editor snippet and is not part of the assignment solution.

## How to Run

1. Extract the ZIP archive.
2. Open a terminal in the extracted assignment folder.
3. Run each program separately:

```bash
python discount_rule.py
python loop_control.py
python process_multiple_orders.py
python user_menu.py
```

On systems where the Python command is `python3`, use `python3` instead.

## Using the Menu Program

Run `user_menu.py`, then choose:

- `1` – Enter and add an order amount.
- `2` – Display all entered orders, their discounts, and the total revenue.
- `q` – Exit the program.

## Notes

- Each program is independent and can be executed separately.
- The examples use in-memory data; no database or external package is required.
- `discount_rule.py` checks for digit-only input. The menu program expects a valid integer when adding an order amount.
