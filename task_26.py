# Задача 26:Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

while True:
    try:
        a = int(input("Введите число: "))
        b = int(input("Введите его степень: "))

        def power(a, b):
            if b == 0:
                return 1
            if (b == 1):
                return (a)
            if (b != 1):
                return (a * power(a, b - 1))

        print("Результат возведения в степень равен:", power(a, b))
        break
    except:  
         print('Некорректный ввод. Введите еще раз!')