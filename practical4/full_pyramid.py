rows = 5

for i in range(1, rows + 1):
    # spaces (center alignment)
    print(" " * (rows - i), end="")

    # stars
    for j in range(i):
        print("* ", end="")

    print()

for i in range(rows):
    # spaces
    print(" " * i, end="")

    # alphabets
    for j in range(rows - i):
        print(chr(65 + j), end=" ")

    print()