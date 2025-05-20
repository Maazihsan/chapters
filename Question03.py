# Glossary dictionary with programming terms and their meanings
glossary = {
    'variable': 'A named location used to store data in memory.',
    'function': 'A block of code that performs a specific task.',
    'loop': 'A control structure that repeats a block of code multiple times.',
    'list': 'An ordered collection of items which can be changed.',
    'dictionary': 'A collection of key-value pairs used to store data.'
}

# Print each word and its meaning with formatting
for word, meaning in glossary.items():
    print(f"{word.capitalize()}:\n  {meaning}\n")
