import json
import os

folder = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(folder, "cities.json")

if not os.path.exists(filename) or os.path.getsize(filename) == 0:
    start = {
        "Запоріжжя": 710052,
        "Мелітополь": 150768,
        "Бердянськ": 107928,
        "Енергодар": 53496,
        "Токмак": 28741,
        "Кам'янка-Дніпровська": 23660,
        "Пологи": 18452,
        "Оріхів": 14134,
        "Вільнянськ": 14048,
        "Гуляйполе": 12904
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(start, f, ensure_ascii=False, indent=4)

with open(filename, "r", encoding="utf-8") as f:
    cities = json.load(f)

while True:
    print()
    print("1 - вивести населення міста")
    print("2 - вивести всі міста за спаданням населення")
    print("3 - додати місто")
    print("0 - вихід")
    choice = input("Оберіть дію: ")

    if choice == "1":
        name = input("Введіть назву міста: ")
        if name in cities:
            print(name, ":", cities[name])
        else:
            print("Такого міста немає у файлі")
    elif choice == "2":
        for name, people in sorted(cities.items(), key=lambda x: x[1], reverse=True):
            print(name, ":", people)
    elif choice == "3":
        name = input("Введіть назву міста: ")
        people = int(input("Введіть населення: "))
        cities[name] = people
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(cities, f, ensure_ascii=False, indent=4)
        print("Місто додано")
    elif choice == "0":
        break
