def read_content(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def write_content(filename: str, content: str) -> None:
    with open(filename, "w") as f:
        f.write(content)


filename = "sales_data.txt"
sales = [1200, 450, 980, 1500, 3000]

content = "\n".join(str(sale) for sale in sales)

write_content(filename, content)
print(read_content(filename))
