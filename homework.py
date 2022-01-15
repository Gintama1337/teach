import numpy as np
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
dct = {'el7':[7, 5, 6]}
print(dct)
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


