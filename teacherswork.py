from random import randint
##==//Работа с условными значениями//==
aa = None
aaa = 'str'
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
    4*3 *2*1*1"""
    if n == 0:
        return 1
    return n * factorial(n-1) # 4 * factorial(n-1=3) -> 12 *
print(factorial(4))
# ДЗ: СДЕЛАТЬ СВОЙ ФАКТОРИАЛ В ЦИКЛЕ

# cc = 4
# for i in range(1, c):
    # c += i #c = c+i
    # c *= i #c = c*i
    # c /= i #c = c/i
    # print(c)
# print(c)
