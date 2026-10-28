import csv
import os
import string

folder = os.path.dirname(os.path.abspath(__file__))
article = os.path.join(folder, "article.txt")

if not os.path.exists(article) or os.path.getsize(article) == 0:
    sample = ("Python is a popular programming language. Python is easy to learn, "
              "and many students use Python.\n"
              "A language can be simple. Learning a language takes time, "
              "but the language is fun!\n")
    with open(article, "w", encoding="utf-8") as f:
        f.write(sample)

f = open(article, "r", encoding="utf-8")
text = f.read().lower()
f.close()

words = []
for w in text.split():
    words.append(w.strip(string.punctuation))

keywords = input("Введіть 3-4 ключові слова через пробіл: ").lower().split()

with open(os.path.join(folder, "number.csv"), "w", newline="", encoding="utf-8-sig") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    for k in keywords:
        writer.writerow([k, words.count(k)])

print("Готово. Результат у файлі number.csv")
