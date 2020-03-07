# ------------- task 1

print("\n task1\n")

"""
1. Создать программно файл в текстовом формате, 
записать в него построчно данные, 
вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка.
"""

file = open("task1.txt" , "w")

while True:

    string = input("Enter new line\n")

    if string == "":
        break
    else:
        string += '\n'
        file.write(string)

file.close()


# ------------------ task2


print("\n task2\n")

"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.

"""

count_line = 0
count_words = 0

try:
    with open("task2.txt" , "r") as file:
        for line in file:
            count_line += 1
            count_words = len(line.split(" "))
            print(f"In line {count_line} there are {count_words} words\n")

    print(f"In total there are {count_line} lines")
except IOError:
    print("File not exist")


# --------------task 3

print("\n task 3\n")

"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

def some_calculation(list):

    print("Employers that have salary less then 20 000 \n")
    count = len(list)
    average = 0
    try:
        for data in list:
            line = data.split(" ")
            average += int(line[1])
            if int(line[1]) < 20000:
                print(f"{line[0]}\n")
    except ValueError:
        print("Value error in some_calculation func")

    print(f"Average salary = {round(average/count , 2)}")


try:
    file = open("task3.txt", "a+")
    while True:
        lastname = input("Enter lastname or press Enter to finish\n")
        if lastname != "" :
            salary = input("Enter salary\n")
            file.write(f"{lastname} {salary}\n")
        else:
            break

    file.seek(0)
    data = file.readlines()

    file.close()
    some_calculation(data)

except IOError:
    print("File not exist")



# --------------task 4

print("\n task4\n")

"""

4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу,
открывающую файл на чтение
и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

translate = {"One" : "Один" , "Two" : "Два" , "Three" : "Три" , "Four" : "Четыре"}

def rename_func(list):
    try:
        list[0] = translate.get(list[0])
    except ValueError:
        print("Value error in rename_func\n")

    return list

try:
    new_file = open("change.txt", "w" , encoding="utf8")
    with open("task4.txt" , "r") as file:
        for line in file:
            line = rename_func(line.split(" "))
            new_file.write(" ".join(line))
            print(line)
    new_file.close()
except IOError:
    print("File not exist")

# --------------- task 5

print("\n task 5\n")


"""
5. Создать (программно) текстовый файл,
записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

def summ(list):
    try:
        summ = 0
        for el in list:
            summ += int(el)
        return summ
    except ValueError:
        return "Need type of list"

try:
    file = open("task5.txt" , "w+")
    length = int(input("Enter the lenght of the list\n"))

    for i in range(length-1):
        file.write(f"{randint(1 , 100)} ")
    file.write(f"{randint(1, 100)}")

    file.seek(0)
    data = file.readline().split(" ")
    print(data)
    result = summ(data)
    file.close()

    print(f"The summ of elements = {result}\n")

except IOError:
    print("File not exist")

except ValueError:
    print("Need integer!")

# -------------task 6

print("\n task 6\n")

"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

"""

def count_lessons(list):
    try:
        summ = 0
        for el in list[1:]:
            if el[0] != '-' and el != ['-\n']:
                summ += int(el[0])
        return summ
    except ValueError:
        return "Value Error"

def read_data():
    try:
        file = open("task6.txt" , "r" , encoding="utf8")
        data = file.readlines()
        file.close()
    except IOError:
        return "IO error"

    return data

def get_info(file_data):
    try:
        for line in file_data:
            data = line.split(" ")
            for i in range(len(data)):
                data[i] = data[i].split("(")
            yield data
    except ValueError:
        yield "Value error"

dict = {}
for el in get_info(read_data()):
    dict.update({str(el[0])[2:-3] : count_lessons(el)})

print(dict)

# ---------------task 7

print("\n task 7\n")


"""
7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""



# ------------------ task 7

print("\n task 7\n")

import json

try:
    count = 0
    average = 0
    dict_firms = {}
    with open("task7.txt"  , "r" , encoding="utf8") as file:
        for line in file:
            data = line.split(" ")
            profit = int(data[2]) - int(data[3])
            if profit > 0:
                average += profit
                count += 1
            dict_firms.update({data[0] : profit})
    dict_avg = { "average_profit" : round(average/count , 2)}
    result = [dict_firms , dict_avg]
    print(result)

    with open("json_result.json" , "w" , encoding="utf8") as file:
        json.dump(result , file)

except IOError:
    print("File not exist")
except ValueError:
    print("Value Error")


