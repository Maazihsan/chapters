# Dictionaries representing different pets
pet1 = {
    'animal': 'dog',
    'owner': 'Emily'
}

pet2 = {
    'animal': 'cat',
    'owner': 'Carlos'
}

pet3 = {
    'animal': 'parrot',
    'owner': 'Aisha'
}

# List of pets
pets = [pet1, pet2, pet3]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"Animal: {pet['animal'].capitalize()}")
    print(f"Owner: {pet['owner']}")
    print()  # Blank line for readability
