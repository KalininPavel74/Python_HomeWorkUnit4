# Калинин Павел 24.12.2022
# Знакомство с языком Python (семинары) 
# Урок 4. 
# Домашняя работа

from math import pi, sqrt
import random

taskName = '''Задание  №1. Вычислить число c заданной точностью d.
           '''
"""
Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""
isRepeat = True
while(isRepeat): 
    print("-----------------------------------\n\r"+taskName)
    a = int(input('Введите требуемую точность вычисления - целое число: '))
    #--------------
    print('Ответ:')
    print(f'π={round(pi,a)}')
    print(f'1,000,000/3={round(1_000_000.0/3.0,a)}')
    s = input('\n\r----\n\rВыполнить задание еще раз? (0-нет, 1-да):')
    isRepeat = s != '0'
#------

taskName = '''Задание  №2. Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N.
           '''
count_division = 0 # кол-во делений
# поиск числа множителя, которое может встретиться несколько раз
def find_multiplier(N, multiplier, end, prime_multiplier):
    global count_division
    count_division+=1
    while N>=multiplier and not N % multiplier: # если простой множитель повторяется
        N=N//multiplier
        prime_multiplier.append(multiplier)
        end = int(sqrt(N))+1  # скорректировать макс.
        count_division+=1
    return N, end

isRepeat = True
while(isRepeat): 
    print("-----------------------------------\n\r"+taskName)
    Number = int(input('Введите натуральное число: '))
    N = Number # рабочее число
    count_division = 0 # кол-во делений
    prime_multiplier = []
    end = int(sqrt(N))+1
    N, end = find_multiplier(N, 2, end, prime_multiplier)
    if N>2:
        # перебор нечетных чисел
        begin = 3 # начальное нечетное число, т.к. двойка проверена
        i = begin
        while i < end:
            N, end = find_multiplier(N, i, end, prime_multiplier)
            i+=2
    # если что-то осталось, то это последний множитель
    if N!=1: prime_multiplier.append(N)
    s = '1'
    testN = 1
    for i in prime_multiplier:
        s += ' * '+str(i)
        testN *= i
    if Number != testN:
        print(f'Тест не прошел: {Number} != {testN}')
    #--------------
    print('Ответ:')
    print(Number, '=', s) 
    print('         (Кол-во делений:', count_division,')') 
    s = input('\n\r----\n\rВыполнить задание еще раз? (0-нет, 1-да):')
    isRepeat = s != '0'
#------
#i= 10 000 000 count= 242 2 626 033


taskName = '''Задание  №3. Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся 
элементов исходной последовательности.
           '''
isRepeat = True
while(isRepeat): 
    print("-----------------------------------\n\r"+taskName)
    s = input('Введите последовательность чисел, через символ пробела: ')
    list1 = s.split(' ')
    list2 = []
    if len(list1):
        list1 = list(map(lambda x: float(x), list1))
        list1.sort()
        flag_double = False # пошли двойники
        temp = list1[0]
        for x in list1[1:]: 
            if temp == x:
                flag_double = True # пошли двойники
            else: # переход к новому значению
                if not flag_double: # если двойников не было
                    list2.append(temp)
                flag_double = False 
                temp = x    
        if not flag_double: # включить последнее значение, если двойников не было
            list2.append(list1[-1])
    print('Ответ:')
    print(list2)
    s = input('\n\r----\n\rВыполнить задание еще раз? (0-нет, 1-да):')
    isRepeat = s != '0'
#------


taskName = '''Задание  №4. Задана натуральная степень k. 
Сформировать случайным образом 
список коэффициентов (значения от 0 до 100) многочлена 
и записать в файл многочлен степени k.
           '''
"""
Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""

def koef_polinomial_to_str(list1):
    len_list = len(list1)
    s = ''
    for i,v in enumerate(list1):
        v_s_not1 = str(v) if v!=1 else ''
        if i == len_list-1 and v:
            s += str(v)
        elif i == len_list-2 and v:
            s += v_s_not1 + 'x + '           
        elif v:
            s += v_s_not1 + 'x^' + str(len_list - i - 1) + ' + '
    if s.endswith(' + '): s=s[:-3]
    if len_list <= 1 or not s: s = 'это не многочлен'
    else: s += ' = 0'       
    return s


isRepeat = True
while(isRepeat): 
    print("-----------------------------------\n\r"+taskName)
    k = int(input('Введите степень многочлена - натуральное число: '))
    list1 = [random.randint(0,100) for _ in range(k+1)]
    list1[0] = random.randint(1,100)
    s = koef_polinomial_to_str(list1)
    #--------------
    print('Ответ:')
    print(s)
    print("Сохранение в файл file0.txt")
    with open('file0.txt', 'w', encoding='utf-8') as f:
        f.write(s)
    print("Чтение из файла file0.txt")
    list_file0: list[str]
    with open('file0.txt', 'r', encoding='utf-8') as f:
        list_file0 = f.readlines()
    print(list_file0[0])

    s = input('\n\r----\n\rВыполнить задание еще раз? (0-нет, 1-да):')
    isRepeat = s != '0'
#------


taskName = '''Задание  №5. Даны два файла, 
в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
           '''

def parse_to_koef_list(s):
    s_left = s.split('=')[0]
    list1 = s_left.split('+')
    list1 = list(map(lambda s: s.strip(), list1))
    # найти максимальную степень многочлена
    degree_max = -1
    if list1[0].find('x') != -1:
        index = list1[0].find('x^')
        if index == -1: 
            degree_max = 1
        else: degree_max = int(list1[0][index+2:])
        # создать новый лист
            # предзаполнить нулями
        list2 = [0 for _ in range(degree_max+1)]
        # заполнить значениями в соответствии со степенями    
        for s in list1:
            degree = None
            index = s.find('x^')
            if index != -1: 
                degree = int(s[index+2:])
                if not s[:index]: koef = 1
                else: koef = int(s[:index])
            elif s.find('x') != -1: 
                degree = 1
                koef = int(s[:s.find('x')])
            else: 
                degree = 0
                koef = int(s)
            list2[degree_max-degree] = koef # максимальная степень располагается в 0 ячейке
    return list2

isRepeat = True
while(isRepeat): 
    print("-----------------------------------\n\r"+taskName)
    print("Чтение многочлена из файла file1.txt")
    list_file1: list[str]
    list_file2: list[str]
    with open('file1.txt', 'r', encoding='utf-8') as f:
        list_file1 = f.readlines()
        print(list_file1[0])

    print("Чтение многочлена из файла file2.txt")
    with open('file2.txt', 'r', encoding='utf-8') as f:
        list_file2 = f.readlines()
        print(list_file2[0])

    list1 = parse_to_koef_list(list_file1[0])
    list2 = parse_to_koef_list(list_file2[0])

    if list_file1[0] != koef_polinomial_to_str(list1): 
        print('1. Проверка не прошла')
    if list_file2[0] != koef_polinomial_to_str(list2): 
        print('2. Проверка не прошла')

    # суммировать многочлены
    list1.reverse()
    list2.reverse()
    len_list1 = len(list1)
    len_list2 = len(list2)
    if len_list1 > len_list2:
        list2 = list2 + [0 for _ in range(len_list1 - len_list2)]
    else:    
        list1 = list1 + [0 for _ in range(len_list2 - len_list1)]
    for i in range(len(list1)):
        list1[i] += list2[i]
    list1.reverse()
    list_sum = list1

    #--------------
    print('Ответ:')
    print(koef_polinomial_to_str(list_sum))
    #s = input('\n\r----\n\rВыполнить задание еще раз? (0-нет, 1-да):')
    #isRepeat = s != '0'
    isRepeat = False
#------
