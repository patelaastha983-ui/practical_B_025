# Even Numbers between 1 to 100

even_numbers = []

for num in range(1, 101):
    if num % 2 == 0:
        even_numbers.append(num)

print("List of even numbers:")
print(even_numbers)

print("Minimum even number:", min(even_numbers))
print("Maximum even number:", max(even_numbers))
print("Sum of even numbers:", sum(even_numbers))