import numpy as np
import re
import random
from random import randint
from matplotlib import pyplot as plt
import math
from datetime import datetime
import timeit

#HW1

def hw_cycle(n:int)->int:
    """
    Функция считает факториал целочисленного числа
    через цикл For
    """
    if n == 0:
        n = 1
    else:
        for i in range(n-1):
            n = (i+1) * n
    return n

# print(hw_cycle(5))

#HW2

hw_dict = {'el0':0, 'el1':30, 'el2':60, 'el3':80, 'el4':10, 'el5':90}
def hw_sin(hw_dict:dict)->dict:
    """
    Функция принимает словарь
    и высчитывает синус каждого значения
    этого словаря, а после возвращает
    копию этого списка с значениями равными
    синусом прошлых значений
    """
    for key in hw_dict:
        hw_dict[key] = np.sin(hw_dict[key]*np.pi/180)
        # print(key)
        # print(hw_dict[key])
    return hw_dict
# print(hw_sin(hw_dict))
# print(hw_dict['el3'])
# print(hw_sin(hw_dict))
# hw_dict.update()
# print(*hw_dict)
# dct = {'el7':[7, 5, 6]}
# print(dct)

#HW3

def random_list_3el(j, t, p:int)->list:
    """
    Функция создает случайный список и при помощи цикла While
    удаляет в нём значения до тех пор пока не останется 3 значения.
    """
    lst = [randint(j, t) for i in range(p)]
    while len(lst) != 3:
        lst.pop()
        continue
    return lst
# print (random_list_3el(5, 10, 20))

#HW4

def sin_cos_showoff(hw_dict:dict):
    """
    Функция принимает на вход словарь
    и выводит график sin и cos значений этого словаря
    """
    graf_sin = []
    graf_cos = []
    for key in hw_dict:
        graf_sin.append(np.sin(hw_dict[key]))
        graf_cos.append(np.cos(hw_dict[key]))
    plt.plot(graf_sin)
    plt.plot(graf_cos)
    return plt.show()
# print(sin_cos_showoff(hw_dict))

#HW6

# any_dict = {}
# for i in range(5):
#     key = input()
#     value = randint(0, 999999)
#     any_dict[key] = value
#
# with open('files/usersID.json', 'a') as uID:
#     print(any_dict, file=uID)
#     any_dict_sort = list(any_dict.keys())
#     any_dict_sort.sort()
#     for i in any_dict_sort:
#         print(i, ':', any_dict[i])
    # uID.write(uID for key in randint(0,999999))
    # print((uID for key in random.choices(population='agdgeghsdh')), file=uID)
    # dict_from_uID = {'user1':'','user2':'','user3':'','user4':'','user5':''}
    # def dict_uID_with_randint_key(dict_from_uID:dict):
    #     """
    #     Функция принимает словарь и с помощью
    #     цикла for добавляет случайное числовое значение
    #     к каждому ключу, а после запиывает этот словарь
    #     в файл userID.json
    #     """
    #     for key in dict_from_uID:
    #         dict_from_uID[key] = randint(0, 999999)
    #     return dict_from_uID
    # print(dict_uID_with_randint_key(dict_from_uID), file=uID)
    # print(re.search('\w', 'files/usersID.json'))
    # print(uID.read())





#HW7

test_string = "aaa mayonez suka ketchup huy suka blyad aaa dodik MANDA MagaZin suka "
# get_some_words_to_string = str(input())
# test_string = test_string + get_some_words_to_string.upper()
# print(test_string)

#HW8

def repetition_finder(test_string:str)->list:
    """
    Функция принимает строку и считает колличество повторений слов
    далее возвращает слово и колличество его повторений
    """
    repetition = re.findall('[a-zA-Z]{,}''\s+', test_string)
    string_and_count = []
    for i in repetition:
        if i in string_and_count:
            continue
        elif repetition.count(i) >= 0:
            string_and_count.append(i)
            repetition.remove(i)
            string_and_count.append(repetition.count(i))
    return string_and_count
# print(repetition_finder(test_string))

#HW9

a, b, c = 1, -2, -24
quadratic_root = []

discr = lambda a, b, c : (b**2)-4*a*c

def kvur_withdiscr(discr:int)->list:
    """
    Функция принимает на вход lambda функцию,
    и в зависимости от значения это функции
    выводит корень уравнения либо их список.
    """
    if discr(a, b, c) < 0:
        return "Уравнение не имеет корней"
    elif (discr(a, b, c)) == 0:
        x = (-b) / (2 * a)
        return x
    elif (discr(a, b, c)) > 0:
        x1 = (-b + ((discr(a, b, c)) ** (0.5))) / (2 * a)
        x2 = (-b - ((discr(a, b, c)) ** (0.5))) / (2 * a)
        quadratic_root.append(int(x1))
        quadratic_root.append(int(x2))
        return quadratic_root


def kvur_graf(kvur_withdiscr:list):
    """
    Функция рисует график на основе данных
    функции kvur_withdiscr
    """
    plt.plot(quadratic_root)
    plt.show()

print (kvur_withdiscr(discr))
print (kvur_graf(kvur_withdiscr))

#HW10

list_to_sort = [5, 3, 6, 2, 5, 6]

# def my_sort(list_to_sort:list)->list:
for i in range(0, len(list_to_sort)):
    for j in range(i+1, len(list_to_sort)):
        if list_to_sort[i] > list_to_sort[j]:
            list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
# return list_to_sort

# print(list_to_sort)

#HW SBER

black_list = [0, 1, 0, 2, 1, 0 ,1, 3, 2, 1, 2, 1]
# 4, 2, 0, 3, 2, 5, 0, 1

# def waterline(black_list:list)->int:
# """
# Функция принимает на вход список
# и возвращает число заполненых пустот между
# максимумов принимаемого списка
# """
highground = []
water_list = 0


for i in range(len(black_list)):
    if black_list[i] != 0:
        highground.append(black_list[0])
        break
    else:
        highground.append(black_list[1])
        black_list.pop(black_list[i])
        break

t = 0
for i in range(1, len(black_list)-1):
    if black_list[i] < highground[t]:
        continue
    elif black_list[i] >= highground[t]:
        highground.append(black_list[i])
        t += 1
highground.append(black_list[-1])

c = 0

for i in range(1, len(black_list)-1):
    if highground[c+1 - len(highground)] == black_list[i]:
        c += 1
    elif highground[c - len(highground)] > highground[c+1 - len(highground)]:
        c += 1
        water_list += highground[c - len(highground)] - black_list[i - len(black_list)]
    else:
        water_list += highground[c - len(highground)] - black_list[i]

# return water_list


# print (water_list)

#HW 11

def divide_in_percent(function):
    def wrapper(*args,**kwargs):
        result = function(*args,**kwargs)
        if (result * 100) < 0:
            return "Числа должны быть положительные"
        elif (result * 100) > 100:
            return 100
        elif (result * 100) >= 0 or (result * 100) <= 100:
            return int(result * 100)
        return result
    return wrapper

@divide_in_percent
def divide(a:int, b:int)->int:
    """
    Делит 2 числа
    """
    return a/b

# print (divide(3, 9))

#HW 12
#HW 12.1 (моя сортировка(похожа на сортировку вставками))

time_test1 = """
list_to_sort = [9,2,7,1,3,6,9,0,1,5,4,7,9]
for i in range(0, len(list_to_sort)):
    for j in range(i+1, len(list_to_sort)):
        if list_to_sort[i] > list_to_sort[j]:
            list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
"""
#~8-10 sec
# print(timeit.timeit(time_test1))

#HW 12.2 (ортировка вставками)

time_test2 = """
my_list = [9,2,7,1,3,6,9,0,1,5,4,7,9]
for i in range(1,len(my_list)):
    top = i-1
    while top:
        if my_list[top]<my_list[top-1]:
            my_list[top-1],my_list[top]=my_list[top],my_list[top-1]
        top-=1
"""
#~8-8.5 sec
# print(timeit.timeit(time_test2))

#HW 12.3 (Сортировка методом выбора)

time_test3 = """
my_list = [9,2,7,1,3,6,9,0,1,5,4,7,9]

for i in range(len(my_list)-1):
    for j in range(i+1, len(my_list)):
        if my_list[j]<my_list[i]:
            my_list[i],my_list[j]=my_list[j],my_list[i]
"""
#~8-9 sec
# print(timeit.timeit(time_test3))

#HW 12.4 (Сортировка пузырьками)

time_test4 = """
my_list = [9,2,7,1,3,6,9,0,1,5,4,7,9]

for i in range(1,len(my_list)):
    for j in range(0,len(my_list)-i):
        if my_list[j]>my_list[j+1]:
            my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
"""
#~10-11 sec
# print(timeit.timeit(time_test4))

#HW 12.5 (Быстрая сортировка - сортировка Тони Хоара)

time_test5 = """
my_list = [9,2,7,1,3,6,9,0,1,5,4,7,9]
def quick_sort(array:list)->list or None:
    if len(array)<=1:
        return
    barrier=array[0]
    L=[]
    M=[]
    R=[]
    for elem in array:
        if elem<barrier:
            L.append(elem)
        elif elem==barrier:
            M.append(elem)
        else:
            R.append(elem)

    quick_sort(L)
    quick_sort(R)

    k=0
    for i in L+M+R:
        array[k]=i
        k+=1
    return array
"""
#~0.2 sec
# print(timeit.timeit(time_test5))

