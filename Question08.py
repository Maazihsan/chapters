# Dictionary with names as keys and lists of favorite places as values
favorite_places = {
    'Alice': ['Paris', 'New York', 'Tokyo'],
    'Bob': ['Sydney', 'Rome'],
    'Carol': ['London', 'Barcelona', 'Maui']
}

# Loop through the dictionary and print each person's favorite places
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"  - {place}")
    print()  # Blank line for readability
