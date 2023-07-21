# Seminar 1

# print('Hello world!', end=' ')

# name = 'Alex'

# name = input('Введите имя: ')
# surname = input('Введите фамилию: ')
# print('Здравствуйте, ' + name + ' ' + surname)
# print('Здравствуйте,', name, surname)
# print(f'Здравствуйте, {name} {surname}')

# a = 'Hello'
# print(type(a), a)
# b = 13
# print(type(b), b)
# c = 3.45
# print(type(c), c)
# d = True
# print(type(d), d)

# a = 15
# b = 7
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)

# print(a < b)
# print(a > b)
# print(a <= b)
# print(a >= b)
# print(a == b)
# print(a != b)


# a = int(input('Введите число: '))
# if a > 0:
#     if a % 2 == 0:
#         print(f'Число {a} четное положительное!')
#     else:
#         print(f'Число {a} нечетное положительное!')
# elif a == 0:
#     print('Число равно 0')
# else:
#     if a % 2 == 0:
#         print(f'Число {a} четное отрицательное!')
#     else:
#         print(f'Число {a} нечетное отрицательное!')

# print('Hello world')

# """За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
#
# Input:
# n = 700
# m = 750
# Output:
# 2
#
# Input:
# n = 700
# m = 1400
# Output:
# 2
# """

# n = int(input())
# m = int(input())
#
# # print(m // n + 1 % (m % n + 1))
#
# print((-m) // n * -1)

# """Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22 (ввод чисел НЕ в одну строку) 21 21 20
# Output: 32
# """
#
# a = int(input('Введите кол-во учеников в первом классе: '))
# b = int(input('Введите кол-во учеников во втором классе: '))
# c = int(input('Введите кол-во учеников в третьем классе: '))
#
# res_a = a // 2 + a % 2
# res_b = b // 2 + b % 2
# res_c = c // 2 + c % 2
# print(f'{res_a} + {res_b} + {res_c} = {res_a + res_b + res_c}')
#
# print(((-(a)) // 2 * -1) + ((-(b)) // 2 * -1) + ((-(c)) // 2 * -1))
#
#
# """Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES
# """

# year = int(input('Введите год: '))
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('YES')
# else:
#     print('NO')

# Seminar 2

# Цикл While

# Выведите слово Hello 10 раз

# i = 0
# while i < 10:
#     print('Hello')
#     i += 1


# Вводятся числа, пока не введут 0. Определите кол-во четных чисел из введенной последовательности

# count = 0
# while True:
#     number = int(input())
#     if number == 0:
#         break
#     if number % 2 == 0:
#         count += 1
# print(count)

# count = 0
# number = int(input())
# while number != 0:
#     if number % 2 == 0:
#         count += 1
#     number = int(input())
# print(count)

# Цикл for
# Переменная - итератор используется

# for i in 'hello world!':
#     print(i)

# for j in range(5):  # 0, 1, 2, 3, 4
#     print(j)

# for j in range(5, 10):
#     print(j)

# for j in range(5, 10, 2):
#     print(j)

# for j in range(10, 5, -1):
#     print(j, end=' ')


# some_str = 'привет мир!'
# # for i in some_str:
# #     print(i)
#
# for ind in range(0, len(some_str), 2):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#     print(some_str[ind])
#
# for ind in range(len(some_str) - 1, -1, -1):
#     print(some_str[ind], end='')

# Переменная итератор не используется

# Вывести hello 10 раз

# for _ in range(10):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#     print('hello')

# Вывести слово hello n раз

# n = int(input())
# for _ in range(n):
#     print('hello')

# Вводится кол-во чисел, затем сами числа. Найти произведение нечетных чисел.

# n = int(input('Введите кол-во чисел: '))
# q = 1
# for _ in range(n):  # 0, 1, 2, 3, 4, 5
#     x = int(input('Введите число: '))
#     if x % 2 != 0:
#         q = q * x
# print(q)

# """Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 """

# """Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6"""

# a = int(input())
# first = 0
# second = 1
# temp = first + second
# count = 3
# while temp < a:
#     first = second
#     second = temp
#     temp = first + second
#     count += 1
# if temp == a:
#     print(count)
# else:
#     print(-1)

# """Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2
# """

# n = int(input('Введите кол-во дней: '))
# count = 0
# max_count = 0
# for _ in range(n):
#     temp = int(input('Введите температуру: '))
#     if temp > 0:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#         count = 0
# if count > max_count:
#     max_count = count
# print(max_count)

# """Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 2 6 5 9
# Output: 2 9
# """

# n = int(input('Введите кол-во арбузов: '))
# minn = int(input('Введите вес арбуза: '))
# maxx = 0
# for _ in range(n - 1):
#     weight = int(input('Введите вес арбуза: '))
#     if weight > maxx:
#         maxx = weight
#     if weight < minn:
#         minn = weight
# print(minn, maxx)


# Seminar 3

# list
# some_list = []
# print(type(some_list))

# some_list = [1, 4.34, 'hello', True, [1, 2, 3]]
# print(some_list)
#
# print(some_list[-1])
#
# print(some_list[::-1])

# Вводится кол-во чисел, затем сами числа. Добавьте в список только четные числа

# count = int(input('Введите кол-во чисел: '))
# some_list = []
# for _ in range(count):
#     number = int(input())
#     if number % 2 == 0:
#         some_list.append(number)
# print(some_list)

# some_list = [1, 2, True, 'Hello']
#
# for el in some_list:
#     print(el)
#
# for ind in range(0, len(some_list)):
#     print(some_list[ind])


# tuple - кортеж
# some_tuple = tuple(some_list)
# print(some_tuple)
#
# some_tuple = (1, 2, 3, 4)

"""1.Создайте список из случайных чисел.
Найдите индекс его последнего локального максимума
(локальный максимум — это элемент, который больше любого из своих соседей)."""

# import random
#
#
# count = int(input('Введите кол-во элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(0, 10)
#     some_list.append(number)
# print(some_list)

# [1, 10, 2, 0, 7, 4, 8, 5] -> 6
# РЕШЕНИЕ НИЖЕ...

# local_max = None
# for ind in range(1, len(some_list) - 1):
#     if some_list[ind - 1] < some_list[ind] > some_list[ind + 1]:
#         local_max = ind
# print(local_max)

# local_max = None
# for ind in range(len(some_list) - 2, 0, -1):
#     if some_list[ind - 1] < some_list[ind] > some_list[ind + 1]:
#         local_max = ind
#         break
# print(local_max)


# 2.Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.
#
# import random
#
# count = int(input('Введите кол-во элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(0, 10)
#     some_list.append(number)
# print(some_list)

# [9, 1, 2, 6, 10, 6, 7, 4, 10, 2]
# max_count = 0
# for el in some_list:
#     amount = 0
#     for i in some_list:
#         if el == i:
#             amount += 1
#     if amount > max_count:
#         max_count = amount
# print(max_count)

# max_count = 0
# for el in some_list:
#     amount = some_list.count(el)
#     if amount > max_count:
#         max_count = amount
# print(max_count)


# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
"""
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""
# import random
#
# count = int(input('Введите кол-во элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(0, 10)
#     some_list.append(number)
# print(some_list)
#
# new_list = []
# for el in some_list:
#     if el not in new_list:
#         new_list.append(el)
# print(len(new_list))


"""Задача №19. Общее обсуждение
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 2
Output: [4, 5, 1, 2, 3]
"""

# import random
#
# count = int(input('Введите кол-во элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(0, 10)
#     some_list.append(number)
# print(some_list)
#
# k = int(input('Введите число для сдвига: '))
#
# nums = some_list[-k:] + some_list[:-k]
# print(nums)

"""Дан список, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов списка, больших предыдущего (элемента
с предыдущим номером)

Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)"""

# some_list = [0, -1, 5, 2, 3]
# amount = 0
# for ind in range(1, len(some_list)):
#     if some_list[ind - 1] < some_list[ind]:
#         amount += 1
# print(amount)
