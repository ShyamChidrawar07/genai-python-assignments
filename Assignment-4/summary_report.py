def read_sales(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return list(map(int, f.readlines()))


def generate_report(sales: list[int]) -> None:
    total = sum(sales)
    highest = max(sales)
    lowest = min(sales)
    average = total / len(sales)

    print("Sales Summary Report")
    print("--------------------")
    print("Total Sales:", total)
    print("Highest Sale:", highest)
    print("Lowest Sale:", lowest)
    print("Average Sale:", average)


filename = "sales_data.txt"

sales = read_sales(filename)
generate_report(sales)
