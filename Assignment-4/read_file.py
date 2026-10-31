def read_first(filename: str) -> str:
    with open(filename, "r") as f:
        return f.readline()


def read_lines(filename: str) -> list:
    with open(filename, "r") as f:
        data = f.readlines()
        sales = list(map(int, data))
        return sales


def read_file(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read()


filename = "sales_data.txt"

print("Read entire file:", read_file(filename))
print("\nRead Only First Line:", read_first(filename))
print("Read all lines:", read_lines(filename))
