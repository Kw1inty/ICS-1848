import string
import os

folder = os.path.dirname(os.path.abspath(__file__))

f = open(os.path.join(folder, "input.txt"), "r", encoding="utf-8")
text = f.read()
f.close()

digits = open(os.path.join(folder, "digit.txt"), "w", encoding="utf-8")
symbols = open(os.path.join(folder, "symbols.txt"), "w", encoding="utf-8")

for ch in text:
    if ch.isdigit():
        digits.write(ch)
    elif ch in string.punctuation:
        continue
    else:
        symbols.write(ch)

digits.close()
symbols.close()