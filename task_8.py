# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no
import random

while True:
    n = random.randint(1, 10)
    print(f'n = {n}')
    m = random.randint(1, 10) 
    print(f'm = {m}')
    k = random.randint(1, 10) 
    print(f'k = {k}')
    if k < m * n:
        if (k % m == 0 or k % n == 0):
            print(f'Можно ломать!')
            break
        elif k == n * m:
            print('Ломать не нужно!')
            break
        elif k < m or k < n:
            print('За один раз не разломаешь!')
            break
    else:
        print('Столько кусочков нет!')
        break