# Урок 2. Циклы (for, while)

# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input("Введите количество монеток: "))
# o = 0
# r = 0
# for i in range(n):
#     v = int(input("Орел - введите 1. Решка - введите 2: "))
#     if v == 1: o += 1
#     else: r += 1
# if o < r: print(f"Количество монеток, которые нужно перевернуть: {o}")
# elif o == r: print(f"Количество монеток одинаковое")
# else: print((f"Количество монеток, которые нужно перевернуть: {r}"))

# Задача 12: Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# x = int(input("Петя задумал первое натуральное число X (1..1000): "))
# y = int(input("Петя задумал второе натуральное число Y (1..1000): "))
# s = x + y
# p = x * y
# x1 = int((s - ((-s) ** 2 - 4 * p) ** 0.5) / 2)
# y1 = int((s + ((-s) ** 2 - 4 * p) ** 0.5) / 2)
# print(x1, y1)

# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input("Введите число N: "))
# p = 1
# while p <= n:
#     print(p, end = ', ')
#     p = p*2