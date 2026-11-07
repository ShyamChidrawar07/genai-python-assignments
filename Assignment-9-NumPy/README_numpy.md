# NumPy Python Assignment – Array Operations and Sales Analysis

## Overview

This assignment demonstrates the use of NumPy for working with one-dimensional and two-dimensional arrays, performing mathematical calculations, applying aggregation and statistical functions, sorting values, calculating percentiles, and analyzing weekly sales data.

The programs use predefined NumPy arrays and display the results of different operations in the terminal.

## Assignment Task-to-File Mapping

| Task | File | What the program does | Main concepts |
|---|---|---|---|
| Task 1: NumPy arrays | `numpy_array.py` | Creates 1D and 2D arrays using `np.arange()` and displays their shapes and data types. | `np.array()`, `np.arange()`, `reshape()`, `shape`, `dtype` |
| Task 2: Mathematical operations | `mathematical_operations.py` | Performs addition, subtraction, multiplication, division, and exponentiation on two arrays using operators and NumPy functions. | Array arithmetic, broadcasting-compatible operations, `np.add()`, `np.subtract()` |
| Task 3: Mathematical formulas | `numpy_mathematical_formulas.py` | Applies square root, exponential, natural logarithm, sum, and cumulative sum operations to an array. | `np.sqrt()`, `np.exp()`, `np.log()`, `np.sum()`, `np.cumsum()` |
| Task 4: Aggregation operations | `numpy_aggregation_opertions.py` | Calculates row-wise and column-wise sums, minimum, maximum, and overall mean of a 2D array. | `np.sum()`, `axis`, `np.min()`, `np.max()`, `np.mean()` |
| Task 5: Statistical operations | `statiscal_operations.py` | Calculates mean, median, variance, standard deviation, minimum, maximum, and range of student marks. | `np.mean()`, `np.median()`, `np.var()`, `np.std()`, `np.min()`, `np.max()`, `np.ptp()` |
| Task 6: Percentile and sorting | `percentile_and_sorting.py` | Sorts student marks, calculates the 25th, 50th, and 75th percentiles, and counts students scoring above average. | `np.sort()`, `np.percentile()`, `np.mean()`, Boolean comparison, `np.sum()` |
| Task 7: Sales analysis | `sales_analysis.py` | Analyzes weekly sales by calculating total, average, highest, lowest, and standard deviation, then displays sales values above average. | NumPy aggregation, `np.mean()`, `np.max()`, `np.min()`, `np.std()`, loops, conditions |

## Project Structure

```text
Assignment-9-NumPy/
├── mathematical_operations.py
├── numpy_aggregation_opertions.py
├── numpy_array.py
├── numpy_mathematical_formulas.py
├── percentile_and_sorting.py
├── sales_analysis.py
├── statiscal_operations.py
└── README.md
```

## File Details

### 1. `numpy_array.py`

Creates one-dimensional and two-dimensional NumPy arrays and displays their basic properties.

- Creates a 1D array containing values from 1 to 10 using `np.arange(1, 11)`.
- Displays the 1D array.
- Displays its shape using `.shape`.
- Displays its data type using `.dtype`.
- Creates a 2D array containing values from 1 to 9.
- Converts the 2D array into a 3 × 3 matrix using `.reshape(3, 3)`.
- Displays the 2D array, its shape, and its data type.

**Main NumPy functions and attributes:**

- `np.arange()`
- `.reshape()`
- `.shape`
- `.dtype`

### 2. `mathematical_operations.py`

Performs arithmetic operations on two one-dimensional NumPy arrays.

**Input arrays**

```python
A = np.array([10, 20, 30, 40])
B = np.array([1, 2, 3, 4])
```

**Operations using operators**

- Addition: `A + B`
- Subtraction: `A - B`
- Multiplication: `A * B`
- Division: `A / B`
- Power: `A ** 2`

The program also demonstrates NumPy functions for addition and subtraction:

- `np.add(A, B)`
- `np.subtract(A, B)`

The results are calculated element by element because both arrays have the same shape.

### 3. `numpy_mathematical_formulas.py`

Applies mathematical functions to a one-dimensional array.

**Input array**

```python
values = np.array([2, 4, 6, 8, 10])
```

**Operations performed**

- `np.sqrt(values)` – calculates the square root of each element.
- `np.exp(values)` – calculates the exponential of each element.
- `np.log(values)` – calculates the natural logarithm of each element.
- `np.sum(values)` – calculates the sum of all elements.
- `np.cumsum(values)` – calculates the cumulative sum.

The cumulative sum adds each element to the sum of all preceding elements.

### 4. `numpy_aggregation_opertions.py`

Demonstrates aggregation operations on a two-dimensional array.

**Input array**

```python
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

**Operations performed**

- `np.sum(data, axis=1)` – calculates the sum of each row.
- `np.sum(data, axis=0)` – calculates the sum of each column.
- `np.min(data)` – finds the minimum value in the array.
- `np.max(data)` – finds the maximum value in the array.
- `np.mean(data)` – calculates the overall mean.

**Understanding the axis parameter**

- `axis=0` performs the operation column-wise.
- `axis=1` performs the operation row-wise.
- When the axis is omitted, the operation is performed across all elements.

### 5. `statiscal_operations.py`

Performs statistical calculations on a NumPy array containing student marks.

**Input array**

```python
marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])
```

**Statistical operations**

- `np.mean(marks)` – calculates the average marks.
- `np.median(marks)` – calculates the middle value after ordering the data.
- `np.var(marks)` – calculates the variance.
- `np.std(marks)` – calculates the standard deviation.
- `np.min(marks)` – finds the lowest mark.
- `np.max(marks)` – finds the highest mark.
- `np.ptp(marks)` – calculates the range (maximum minus minimum).

### 6. `percentile_and_sorting.py`

Performs sorting and percentile calculations on student marks.

**Input array**

```python
marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])
```

**Operations performed**

- `np.sort(marks)` – returns the marks in ascending order.
- `np.percentile(marks, 25)` – calculates the 25th percentile.
- `np.percentile(marks, 50)` – calculates the 50th percentile (median).
- `np.percentile(marks, 75)` – calculates the 75th percentile.
- `np.mean(marks)` – calculates the average marks.
- `np.sum(marks > np.mean(marks))` – counts the number of students whose marks are above the average.

The expression `marks > np.mean(marks)` creates a Boolean array. NumPy treats `True` as 1 and `False` as 0 when calculating the sum.

### 7. `sales_analysis.py`

Performs a basic analysis of weekly sales data.

**Input array**

```python
sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])
```

**Operations performed**

- Displays the weekly sales array.
- Calculates total weekly sales using the built-in `sum()` function.
- Calculates average daily sales using `np.mean(sales)`.
- Finds the highest sale using `np.max(sales)`.
- Finds the lowest sale using `np.min(sales)`.
- Calculates sales standard deviation using `np.std(sales)`.
- Calculates the average sales and uses a `for` loop with an `if` condition to print sales values greater than the average.

**Implementation note:** The total-sales print statement is written as `print("\nTotal Weekly Sales: ", np, sum(sales))`. This prints the NumPy module object as an additional argument before the total. If only the total is intended, use `print("\nTotal Weekly Sales: ", np.sum(sales))` or `print("\nTotal Weekly Sales: ", sum(sales))`.

The above-average section prints the sales amounts, not the corresponding day names or day numbers.

## Requirements

- Python 3.9 or later
- NumPy
- No other third-party libraries are required.

## How to Run

1. Install Python if it is not already installed.
2. Download or extract the assignment files.
3. Open a terminal in the `Assignment-9-NumPy` directory.
4. Install NumPy:

```bash
pip install numpy
```

5. Run the required Python program.

For example:

```bash
python numpy_array.py
```

Other programs can be run individually:

```bash
python mathematical_operations.py
python numpy_mathematical_formulas.py
python numpy_aggregation_opertions.py
python statiscal_operations.py
python percentile_and_sorting.py
python sales_analysis.py
```

### Windows example

```bat
cd path\to\Assignment-9-NumPy
python sales_analysis.py
```

Each program runs independently and displays its output in the terminal. No database, web server, or external API is required.

## Expected Output

The programs display NumPy arrays and the results of the operations performed on them.

Examples of the program behavior:

- `numpy_array.py` displays a 1D array from 1 to 10 and a 3 × 3 array containing values from 1 to 9, along with their shapes and data types.
- `mathematical_operations.py` displays the element-wise arithmetic results for arrays `A` and `B`.
- `numpy_mathematical_formulas.py` displays the square roots, exponentials, natural logarithms, total sum, and cumulative sum of the input values.
- `numpy_aggregation_opertions.py` displays row sums `[60, 150, 240]`, column sums `[120, 150, 180]`, minimum `10`, maximum `90`, and overall mean `50.0`.
- `statiscal_operations.py` displays statistical measurements for the student marks array.
- `percentile_and_sorting.py` displays the sorted marks, percentile values, and the count of marks above the average.
- `sales_analysis.py` displays weekly sales statistics and the sales amounts greater than the average daily sales. Its total-sales line also prints the NumPy module object because of the current print statement.

## Concepts Demonstrated

- Importing and using the NumPy library
- Creating one-dimensional and two-dimensional arrays
- Generating sequences with `np.arange()`
- Reshaping arrays with `.reshape()`
- Understanding array shape and data type
- Performing element-wise arithmetic operations
- Using NumPy mathematical functions
- Calculating row-wise and column-wise aggregations
- Understanding the `axis` parameter
- Calculating mean, median, variance, and standard deviation
- Finding minimum, maximum, and range
- Sorting array elements
- Calculating percentiles
- Applying Boolean conditions to NumPy arrays
- Counting Boolean results with `np.sum()`
- Using Python loops and conditional statements for data analysis

## Notes

- Each `.py` file is a separate program and should be run individually.
- NumPy must be installed before running the programs.
- The arrays and sales data are predefined in the source code; the programs do not request user input.
- NumPy arithmetic operations are performed element by element when the array shapes are compatible.
- `axis=0` refers to columns and `axis=1` refers to rows for the two-dimensional aggregation example.
- The statistical functions `np.var()` and `np.std()` use NumPy's default population calculation (`ddof=0`).
- The original filenames `numpy_aggregation_opertions.py` and `statiscal_operations.py` are retained as they appear in the assignment archive.
- The total-sales print statement in `sales_analysis.py` can be simplified as described in the file details.
