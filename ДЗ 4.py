# Вычислить число с заданной точностью d
'''
from math import pi
d = int(input("Введите значение точности расчета числа Пи: "))
print(round(pi,d))
'''

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
'''
N = int(input("Введите натуральное число:  "))
list = []
m1 = 2
while N >= m1:
    if N % m1 == 0:
        list.append(m1)
        N = N/m1
    else: m1 +=1
print(list)
'''

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности
'''
list1 = input()
list2 = list1.split()
print(list2)
list3 = []
for i in list2:
    if i not in list3: list3.append(i) 
print(list3)
'''

# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

from random import randint
k = int(input("Введите степень многочлена:  "))

list = [] # создаем список рандомных коэффициентов
for i in range(k+1):
    list.append(randint(1,101))
print(list)

m = '' # создаем запись многочлена
for i in range(len(list)):
    if i != len(list)-1 and list[i] != 0 and i != len(list)-2:
        m += f'{list[i]}x^{len(list)-i-1}'
        if list[i+1] != 0:
            m +='+'
    elif i == len(list)-2 and list[i] != 0:
        m += f'{list[i]}x'
        if list[i+1] != 0:
            m += '+'
    elif i == len(list)-1 and list[i] != 0:
        m += f'{list[i]}=0'
    elif i == len(list)-1 and list[i] == 0:
        m += '=0'
print(m)

file = open('text.txt','w')
file.write(m)


