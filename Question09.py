# Dictionary with names as keys and lists of favorite numbers as values
favorite_numbers = {
    'Alice': [7, 14, 21],
    'Bob': [42, 3],
    'Charlie': [3],
    'Diana': [12, 24],
    'Ethan': [9, 18, 27]
}

# Print each person's favorite numbers
for name, numbers in favorite_numbers.items():
    numbers_formatted = ", ".join(str(num) for num in numbers)
    print(f"{name}'s favorite numbers are: {numbers_formatted}.")
