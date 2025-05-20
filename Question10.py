# Dictionary containing info about each city
cities = {
    'tokyo': {
        'country': 'Japan',
        'population': '37 million',
        'fact': 'It is the largest metropolitan area in the world.'
    },
    'paris': {
        'country': 'France',
        'population': '11 million',
        'fact': 'Known as the "City of Light".'
    },
    'new york': {
        'country': 'USA',
        'population': '19 million',
        'fact': 'Home to the Statue of Liberty.'
    }
}

# Loop through the dictionary and print information about each city
for city, info in cities.items():
    print(f"City: {city.title()}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")
