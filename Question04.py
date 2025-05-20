# Dictionary of rivers and their countries
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Loop to print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.capitalize()} runs through {country.capitalize()}.")

print()  # Blank line for separation

# Loop to print the name of each river
print("Rivers:")
for river in rivers.keys():
    print(river.capitalize())

print()  # Blank line for separation

# Loop to print the name of each country
print("Countries:")
for country in rivers.values():
    print(country.capitalize())
