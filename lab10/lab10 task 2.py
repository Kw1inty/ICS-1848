import os

folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "QUESTIONS")
files = os.listdir(folder)

png_count = 0
for name in files:
    if name.lower().endswith(".png"):
        png_count += 1
print("Кількість файлів .png:", png_count)

print("Файли .jpg (.jpeg):")
for name in files:
    if name.lower().endswith(".jpg") or name.lower().endswith(".jpeg"):
        print(name)

f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tiff.txt"), "w", encoding="utf-8")
for name in files:
    if name.lower().endswith(".tiff"):
        f.write(name + "\n")
f.close()