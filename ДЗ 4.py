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

list1 = input()
list2 = list1.split()
print(list2)
list3 = []
for i in list2:
    if i not in list3: list3.append(i) 
print(list3)
