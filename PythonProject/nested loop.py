rows = int(input("enter # of rows: "))
columns = int(input("enter # of columns: "))
symbol = (input("enter a symbol"))

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()

