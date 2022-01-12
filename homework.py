import numpy as np
from random import randint
from matplotlib import pyplot as plt

#HW1

def hw_cycle(n=1):
    """
    Функция считает факториал целочисленного числа
    через цикл For
    """
    for i in range(n-1):
        n = (i+1) * n
    return n

# print(hw_cycle(5))

#HW2

hw_dict = {'el1':30, 'el2':60, 'el3':80, 'el4':10}
def hw_sin(hw_list):
    """
    Функция принимает словарь
    и высчитывает синус каждого значения
    этого словаря, а после возвращает
    копию этого списка с значениями равными
    синусом прошлых значений
    """
# for key in hw_dict:
#     np.sin(hw_dict.values())
hw_dic = 30
np.sin(hw_dic)
print(hw_dic)

#HW3

def random_list_3el():
    """
    Функция создает случайный список и при помощи цикла While
    удаляет в нём значения до тех пор пока не останется 3 значения.
    """
    lst = [randint(-20, 20) for i in range(20)]
    while True:
        if len(lst) >= 4:
            lst.pop()
        else:
            break
    return lst

#HW4


