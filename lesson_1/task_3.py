"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = int(input("Введите число n: "))
if n < 0:
    print("Введеное число не соответствует целыму положительному!")
else:
    print("n + nn + nnn = " + str(n) + str(n * 2) + str(n * 3))