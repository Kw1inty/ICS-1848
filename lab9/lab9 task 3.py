animals = {
    "вовк": "wolf",
    "лисиця": "fox",
    "ведмідь": "bear",
    "заєць": "hare",
    "їжак": "hedgehog",
    "олень": "deer",
    "білка": "squirrel",
    "лось": "elk",
    "кабан": "boar",
    "борсук": "badger",
    "тигр": "tiger",
    "слон": "elephant"
}

new_animals = {}
for key in animals:
    new_animals[animals[key]] = key

print("Український-англійський словник:")
for key in animals:
    print(key, "-", animals[key])

print("Англійсько-український словник:")
for key in new_animals:
    print(key, "-", new_animals[key])