#-----------------------------task2

print("\n task 2\n")

"""
Представлен список чисел. 
Необходимо вывести элементы исходного списка, 
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""

list = [3 , 2 , 45 , 192 , 2 , 10 , 5 , 7]

# После выполнения должно получиться  [ 45 , 192 , 10 , 7]

new_list = [list[i] for i in range(1 ,len(list)) if list[i] > list[i-1] ]
print(new_list)


#-------------------------task3

print("\n task 3\n")


"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. 
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""

answer = [el for el in range(20 ,241) if el % 20 == 0 or el % 21 == 0 ]
print(answer)


#-------------------------task4

print("\n task 4\n")

"""
Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать итоговый массив чисел, соответствующих требованию. 
Элементы вывести в порядке их следования в исходном списке. 
Для выполнения задания обязательно использовать генератор.
"""

list = [23 , 4 , 6 , 8 , 12 , 23 , 32 , 4 , 4, 8 ,12 , 23 , 1 , 5 , 10]
# После выполнения программы получится список [6 , 32 , 1 , 5 , 10]

new_list = [el for el in list if list.count(el) == 1]
print(new_list)

# Если нужно вывести только уникальные значения

def generator(list):
    try :
        for el in list:
            if list.count(el) == 1 :
                yield el
            else :
                list[list.index(el)] = "#"
    except:
        return "Vallue Error"


new_list = generator(list)

print("\n")
for i in new_list:
    print(i)


# -----------------------task5

print("\n task 5\n")

"""
Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce

def Multiplication(p_el , el):
    return p_el*el

list = [el for el in range(100 , 1001) if el % 2 == 0]


result = reduce(Multiplication , list)

print("Result = " , result , "\n" ,"List = " , list)


# ---------------------------task6

print("\n task 6\n")

"""
 Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

from random import randrange
from itertools import count , cycle
k = 0
start = int(input("Enter start point\n"))
for i in count(start):
    if i > 100:
        break
    print(randrange(i , 2147483647)) # 2147483647 - Предельное значение для знакового типа int

string = "abcdefg"

for i in cycle(string):
    if k > 15:
        break
    else:
        print(i)
        k +=1

# --------------------test7

print("\n task 7\n")


"""
Реализовать генератор с помощью функции с ключевым словом yield, 
создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. 
Функция должна вызываться следующим образом: for el in fibo_gen(). 
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n. 
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from random import randint


def factorial(numb):
    f = 1
    if ( numb != 0):
        for i in range(1 , numb + 1):
            f *= i
    return f

def fibo_gen():
    rand = randint(1 , 100)
    start = randint( 1 , rand)
    obj_gen = (el for el in range(start ,rand))
    try:
        for i in range(15):
            tmp = next(obj_gen)
            yield [ tmp , factorial(tmp) ]
    except:
        yield "StopIteration"

for el in fibo_gen():
        print(el)