import random
import string


def add_punctuation(text):
    result = []
    for word in text.split():
        result.append(word + random.choice(string.punctuation))
    return " ".join(result)


def repeated_words(text):
    words = text.split()
    result = []
    for w in words:
        if words.count(w) > 1 and w not in result:
            result.append(w)
    return result


text = input("Введіть рядок слів, розділених пробілами: ")

print("Рядок із розділовими знаками:")
print(add_punctuation(text))

print("Слова, які повторюються:")
for w in repeated_words(text):
    print(w)
