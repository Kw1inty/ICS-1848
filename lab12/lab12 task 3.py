import digits_module

n = int(input("Введіть натуральне число: "))

print("Сума цифр:", digits_module.digit_sum(n))
print("Найбільша цифра:", digits_module.max_digit(n))
print("Найменша цифра:", digits_module.min_digit(n))
