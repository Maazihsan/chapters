# Dictionary from favorite_languages.py storing who responded and their favorite language
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# List of people who should take the poll (some already responded, some not)
people_to_poll = ['jen', 'mike', 'sarah', 'anna', 'edward', 'john']

# Loop through the list to check if they have taken the poll
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.capitalize()}, for responding to the poll.")
    else:
        print(f"{person.capitalize()}, please take our favorite languages poll!")
