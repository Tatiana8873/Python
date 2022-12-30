# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


import random
number = random.randint(100, 999)
print(number)
a = number % 10
b = number // 10 % 10
c  = number // 100 % 10
print(f'{number} => {a + b + c} ({c} + {b} + {a})')