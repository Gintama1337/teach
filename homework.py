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

def random_list_3el(j, t, p:int)->int:
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

with open('files/usersID.json', 'a') as uID:
    # uID.write(uID for key in randint(0,999999))
    print((uID for key in random.choices(population='agdgeghsdh')), file=uID)

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

