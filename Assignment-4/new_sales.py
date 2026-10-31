def append_file(filename, content):
    with open(filename, "a") as f:
        f.write("\n" + content)


def read_file(filename):
    with open(filename, "r") as f:
        txt = f.read()
        count = len(txt.splitlines())
        return txt, count


new_sales = [5000, 2500, 1700]
filename = "sales_data.txt"

content = "\n".join(str(sale) for sale in new_sales)

append_file(filename, content)

txt, count = read_file(filename)

print("Updated File\n", txt)
print("Number of lines in updated file =", count)
