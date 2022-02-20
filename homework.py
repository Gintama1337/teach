import numpy as np
import re
import random
from random import randint
from matplotlib import pyplot as plt

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



#HW10

any_list = [3, 6, 1, 5, 21]

def sort_any_list(any_list:list)->list:
    any_list.sort()
    return any_list
# print (sort_any_list(any_list))

#HW SBER

black_list = [0, 4, 2, 0, 3, 2, 5]
# 4, 2, 0, 3, 2, 5, 0, 1




def waterline(black_list:list)->int:
    """
    Функция принимает на вход список
    и возвращает число заполненых пустот между
    максимумов принимаемого списка
    """
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

    return water_list


print (waterline(black_list))
