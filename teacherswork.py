from random import randint
##==//Работа с условными значениями//==
aa = None
aaa = 6
# print(f'значение переменной aa = {aa}, а значение aaa = {aaa}')
# print(list(aaa))
# if a == 5:
#     print(True)
# print(a == 5)
# print(bool(a))

#==//Работа с кортежами//==
a = (1, 2, '3', 3)
# print(a)
# print(a.__sizeof__())

#==//Работа с листом//==
b = [1, 2, '3', 3]

# for i in range(len(b)):
#     b[i] = randint(0, 4)
#     b[i] = int(b[i]) + 1
b.append('mayonez')
# print(b)
# print(b.pop())
# print(b)
# for i in range(0, 5, 2): #ранжировка range(start, stop, step)
#     print(i)
# print(len(b))
# print(range(len(b)))

# print(b.__sizeof__())
# print(b[1])

#==//Работа со словарями//==

c = {'k':1, 'd':2, 'f':'3', 'g':4, 'h':5}
# for i in c.keys():
#     c[i] = randint(0, 10)
# print(c.items())
# print(c['d'])
# print(c.values())

# print(c.__sizeof__())

#==//Работа с функциями//==
a = 5
def main(a = 0, b = 0):
    if isinstance(a, str) or isinstance(b, str):
    # if a or b == str: #if a=1=True or b!=str=False
        return 'ты ввёл не то значение индюк'
    else:
        return (a + b) ** 2  # после return ничего не выполняется

    # print((a+b)**2)
# print(main(1, 2))
# print(isinstance(5, str))
# print(bool(5))
# main(5, 6)

#==//Работа с рекурсиями//==
#В РЕКУРСИИ ОБЯЗАТЕЛЬНО ДОЛЖНО БЫТЬ УКАЗАННО УСЛОВИЕ ЗАВЕРШЕНИЯ РЕКУРСИИ.
#n! = факториал = 1*2*3*...*n
def factorial(n:int)->int:
    """это функция считает факториал
    пример:
    4 * factorial(n-1=3)
    3*factorial(n-1=2)
    2*factorial(n-1=1)
    1*factorial(n-1=0)
    factorial(0) return 1
    4*3*2*1*1"""
    if n == 0:
        return 1
    return n * factorial(n-1) # 4 * factorial(n-1=3) -> 12 *
# print(factorial(4))
# ДЗ: СДЕЛАТЬ СВОЙ ФАКТОРИАЛ В ЦИКЛЕ

# cc = 4
# for i in range(1, c):
    # c += i #c = c+i
    # c *= i #c = c*i
    # c /= i #c = c/i
    # print(c)
# print(c)

#==//Работа с исключения//==
"""
    try: 
        сюда вводится код в котором подразумевается ошибка
    except (здесь пишется название ошибки): #без названия ошибки не пишется никогда
        сюда вводится код который надо воспроизвести если произошла 
        ошибка указанная в except
    else:
        сюда вводится код который надо воспроизвести если ошибка 
        не такая как указано в except
    finally:
        сюда вводится часть кода которую нужно выполнить в любом случае
"""
def my_exception(a, b):
    try:
        return (a + b) ** 2  # после return ничего не выполняется
    except Exception:
        return 'долбаеб введи правильно'

# print(my_exception('ривет', 5))


try_find_my_exception = 3536
if try_find_my_exception != 1:
    pass
    # raise TypeError(f'переменная {try_find_my_exception} не равно 1')

#==//Работа с циклами//==
some_list = [3, 4, '5']
# for i, j in enumerate(some_list):
    # print(i, j)
#ДЗ№2 Для цикла for: создать функцию которая будет брать значение
# из словаря и считать значение синуса каждого элемента этого словаря
# а на выходе будет создавать копию словаря с теми же ключами но вместо значний синус этих значений
#abc = {}
#mf(abc)
#ДЗ№3 Для цикла While: создать функцию на вход которой будет поступать список из randint
#и он будет удалять элементы этого списка дор тех пор пока там не останеться 3 элемента

import numpy as np
# from matplotlib import pyplot as plt #as это создание псевдонима для функция
# x = np.arange(0, 2*np.pi, 0.1)
# y = np.sin(x)
# c = np.cos(x)
# t = y/c
# ct = 1/t
# plt.plot(t)
# # plt.plot(ct)
# plt.plot(y)
# plt.plot(c)
# plt.show()
# print(x)
#HW разобраться с sin cos tan cot и вывести графики



#ДЗ№4 Нарисовать график синуса и косинуса из задачи 2

# plt.plot(np.sin(90))
# plt.show()
# 90.*np.pi/180.

# HW5
# разобраться с ебучими **
# разузнать про регулярные выражения

# file = open("files/test.txt", 'a')
# file.write('\nnahui ')
# print(file.read())
# file.close()

# with open("files/test.txt", 'a') as f:
#     f.write('\nlublu')
import json
with open("files/test2.json") as js:
    data = json.load(js)
    print(data)
#HW 6
# создать файлик users где будут клю = имя пользователя, а значение = пароль через randint
# отсортировать словарь и отобрать там значения id
# >>> d = {'a': 10, 'b': 15, 'c': 4}
# >>> list_keys = list(d.keys())
# >>> list_keys.sort()
# >>> for i in list_keys:
# ...     print(i, ':', d[i])

test_string = "aaa mayonez ketchup huy suka blyad aaa dodik MANDA MagaZin"
# search = input()
# len_search = len(search)
# index_start = test_string.find(search)
# index_end = len_search + index_start
# print(index_start, index_end, test_string[index_start:index_end])
# test_string
print(test_string + 'da')
print(test_string)
print('zelenii'*3 + ' her')
# print(len('mayonez'))
# print(test_string[test_string.rfind('mayonez'):test_string.rfind('mayonez')+len('mayonez')])
#ДЗ7 добавить в имеющуюся строку слова с инпут и в верхнем регистре
#ДЗ8 написать функцию которая будет считать колличество повторений слов если нет то 0, да 1 и т.п.



# np.ndarray посмотреть документацию

#HW13
#Написать алгоритм который будет показывать все комбинации чисел
#прим вход 2 выход 0 1 2, 0 2 1 и т.п.
#HW14
# написать функцию которая будет считать корни квадратного уравнения, дискриминант, и рисовать график и
# по правильному входу, после он вводит (а, б, с), пользователь можент указать на выбор что ему из этого нужно, (посчитать дискриминант, график либо всё сразу)
# и весь результат и записать в отдельный файл
