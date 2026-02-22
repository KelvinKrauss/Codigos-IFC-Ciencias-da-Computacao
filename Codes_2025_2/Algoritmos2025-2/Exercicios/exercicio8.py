size = int(input("Enter the size of the arrow (e.g., 4): "))
for i in range(1, size + 1):
    spaces = " " * ((size - i) * 2)
    if i == 1:
        content = "#"
    else:
        dashes = "-" * ((i - 1) * 2)
        content = "#" + dashes
    print(spaces + content)
 
for i in range(size - 1, 0, -1):
    spaces = " " * ((size - i) * 2)
    if i == 1:
        content = "#"
    else:
        dashes = "-" * ((i - 1) * 2)
        content = "#" + dashes
    print(spaces + content)