# Задача 28:Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))


while True:
    try:
        def summa(a, b):
            if b == 0:
                return a
            elif a == 0:
                return b
            elif b > 0:
                return summa(a + 1, b - 1)
            else:
                return summa(a - 1, b + 1)
                
        print("Результат суммы A и B равен:", summa(a, b)) 
        break
    except:  
            print('Некорректный ввод. Введите еще раз!')