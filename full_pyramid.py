rows = 5

for i in range(rows, 0, -1):
    # Print spaces
    for space in range(rows - i):
        print(" ", end="")
    
    # Print stars
    for star in range(i):
        print("*", end=" ")
    
    print()