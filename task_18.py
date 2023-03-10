# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, 
# которое необходимо проверить - X. Заполните массив случайными натуральными числами 
# от 1 до N. Выведите, ближайший к X элемент. Если есть несколько элементов, 
# которые равноудалены от X, выведите наименьший по величине.
# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6
import random 
import math

while True:
    try:
        N = int(input('Введите размер масива: '))
        X = int(input('Введите число которое нужно проверить: '))
        A = [random.randint(1, N) for i in range(N)]
        print(A)
        distance = abs(X - A[0])
        num = A[0]
        for i in range(1, N):
            if abs(A[i] - X) != 0 and distance > abs(A[i] - X):
                distance = abs(A[i] - X)
                num = A[i]
        print(num)
        break
    except:  
         print('Некорректный ввод. Введите еще раз!')