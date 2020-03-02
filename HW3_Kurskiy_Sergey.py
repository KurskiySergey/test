
# -----------------------------------task 1

"""
Реализовать функцию, принимающую два числа
 (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя,
 предусмотреть обработку ситуации деления на ноль.
"""
print("\n task1\n")

def division(a , b):
    if (b == 0):
        return "division on 0!"
    else :
        return round(a/b , 2)

var1 = int(input("Enter numerator\n"))
var2 = int(input("Enter denominator\n"))

print("{} / {}  = {}".format(var1 , var2 , division(var1 , var2)))

# --------------------------------------task 2

print("\n task2\n")

"""
Реализовать функцию, принимающую несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
"""

def personalInfo(**kwargs):
    return kwargs

firstname = input("Enter your firstname\n")
lastname = input("Enter your lastname\n")
birthday = input("Enter your birthday (dd.mm.yyyy)\n")
hometown = input("Enter your hometown\n")
email = input("Enter email\n")
phone = input("Enter phone number\n")

data = personalInfo( Firstname = firstname , Lastname = lastname , Birthday = birthday , Hometown = hometown , Email = email , Phone = phone)

print(data)

# -----------------------------------------task 3

print("\n task3\n")

"""
 Реализовать функцию my_func(),
 которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""

def my_func(var1 , var2 , var3):
    array = [var1 , var2 , var3]
    array.sort()
    return  array[-1] + array[-2]


var1 = int(input("Enter var1\n"))
var2 = int(input("Enter var2\n"))
var3 = int(input("Enter var3\n"))

print("summ = " , my_func(var1 , var2 , var3))


# ------------------------------------task 4

print("\n task4\n")

"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

def powFunc(x , y):
    if y > 0 or x <= 0:
        return "Error! Probably y is positive or x is negative"
    else:
        return x ** y


def powFuncVer2(x , y):
    if y > 0 or x <= 0:
        return "Error! Probably y is positive or x is negative"
    else:
        a = x
        while y < -1:
            y += 1
            x *= a


        return 1/x




print("Find x^y\n")
x = int(input("Enter x\n"))
y = int(input("Enter y\n"))

result = powFunc(x , y)

print("x^y = " ,result)
print("Ver2: x^y = " , powFuncVer2(x , y))

# ------------------------------------------rask 5

print("\n task5\n")

"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
 Но если вместо числа вводится специальный символ,
выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
 то вначале нужно добавить сумму этих чисел к полученной ранее
 сумме и после этого завершить программу.
"""
exit = False

def summary(list):
    summ = 0;
    for i in range(len(list)):
        if list[i] != 'q' :
            summ += int(list[i])
        else :
            global exit
            exit = True
            break

    return summ

result = 0
string = input("Enter string of numbers that are divided by space or Press q to exit\n")
numbers = string.split(" ")
result += summary(numbers)
print( "summ of numbers = " ,result)

while exit != True :
    string = input("Enter new string of numbers that are divided by space or Press q to exit\n")

    numbers = string.split(" ")

    result += summary(numbers)

    print("summ of numbers = " ,result)

print("Finish")

# ----------------------------------task 6

print("\n task6\n")

"""
 Реализовать функцию int_func(),
 принимающую слово из маленьких латинских букв и возвращающую его же,
 но с прописной первой буквой.
 Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(text):
    if str(type(text)) == "<class 'str'>":
        return text.title()
    else :
        return "You need class string!"

text = "test"

print(type(text) , int_func(text))

text = 1

print(type(text) , int_func(text))

text = input("Enter words that are divided by space\n").split(" ")
sentence = ""
for i in range(len(text)):
    text[i] = int_func(text[i])
    sentence = sentence + text[i] + " "

print(type(sentence) , " " , sentence)