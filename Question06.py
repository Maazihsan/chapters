# Dictionary for person 1
person1 = {
    'first_name': 'Emily',
    'last_name': 'Johnson',
    'age': 29,
    'city': 'Seattle'
}

# Dictionary for person 2
person2 = {
    'first_name': 'Carlos',
    'last_name': 'Mendez',
    'age': 35,
    'city': 'Miami'
}

# Dictionary for person 3
person3 = {
    'first_name': 'Aisha',
    'last_name': 'Khan',
    'age': 24,
    'city': 'New York'
}

# List of people dictionaries
people = [person1, person2, person3]

# Loop through the list and print each person's info
for person in people:
    print(f"Name: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()  # Blank line for better readability between people
