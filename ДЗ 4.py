# Задача 1 Вычислить число с заданной точностью d
'''
from math import pi
d = int(input("Введите значение точности расчета числа Пи: "))
print(round(pi,d))
'''
'''
import math
n = input()
length = len(n.split(".")[1])
print(round(math.pi, length))
'''

# Задача 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
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

# Задача 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
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

# задача 4 Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
'''
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
'''

# Задача 5 Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


pol1 = "12*x**8+2*x**6+2*x**4+3*x**3+2*x**2+3"
pol2 = "34*x**25+20*x**11+10*x**7+8*x**4+1*x**3+6*x**1+5"

pol1 = pol1.split("+") # Преобразуем многочлен в строку
pol2 = pol2.split("+") 

print(pol1)
print(pol2)

for indx, value in enumerate(pol1): # убираем из строки *x**, сохраняем только числа и делаем новый список 
    pol1[indx] = list(map(int,value.split("*x**")))
for indx, value in enumerate(pol2): 
    pol2[indx] = list(map(int,value.split("*x**")))

print(pol1)
print(pol2)

result = pol1 + pol2
print(result)

result = sorted(result, key = lambda x: x[1] if len(x)>1 else 0, reverse = True)
print(result)

cur_indx = 0
result_list = []
while cur_indx < len(result) - 1:
    cur_num = result[cur_indx]
    next_num = result[cur_indx+1]
    if len(cur_num) > 1 and len(next_num) > 1:
        if cur_num[1] == next_num[1]:
            sum_koeff = cur_num[0] + next_num[0]
            result_list.append([sum_koeff, cur_num[1]])
            cur_indx +=1    
        else:
            result_list.append(result[cur_indx])
    if len(cur_num) > 1 and len(next_num) == 1:
        result_list.append(result[cur_indx])
    if len(cur_num) == 1  and len(next_num) == 1:
        result_list.append([cur_num[0] + next_num[0]])
    cur_indx +=1

print(result_list)    