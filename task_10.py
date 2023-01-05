# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random
coins = random.randint(5,10)
print(coins)
random_number = [random.randint(0, 1) for i in range(coins)]
print(random_number)
eagle = random_number.count(1)
reshko = random_number.count(0)
if eagle < reshko:
    print(eagle)
else:
    print(reshko)
