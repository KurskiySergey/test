# ------- task 1

print("\n task1\n")

from Task1 import Data

data_1 = Data("12-10-2016")
data_1.full_data
print()
data_2 = Data("12-13-2016")
data_2.full_data
print()
data_2.str_data = "10-06-2020"
data_2.full_data
print()
Data.data_transform(data_2.str_data)
print()
data_2.full_data
print()
data_1.full_data



# ------ task 2

print("\n task2\n")

import Task2

Task2.division()

# ------ task 3

print("\n task3\n")

import Task3

Task3.list_check()


# ----- task 4 , 5 , 6

from OrgRepository import *

# Создаем элементы
printer = Printer(128, 'model-x0123')
# Менеяем параметры классов на нужные
Orgtech.cur__type_discount(Printer, 10)
# Создание склада
rep = Repository()
# Берем на склад элементы в определенном количестве
rep.to_take(printer, 15)
# Получаем информацию о складе
rep.repository_info()
# Получаем информацию о конкретном типе и модели этого типа
rep.element_info('printer' , 'model-x0123')
# Отправляем определенный тип и модель в магазин в определенном количестве
rep.to_send('printer', 'model-x0123' , 'МВидео', 5)
print()
rep.repository_info()

# --- task 7

from ComplexOp import Complex

a = Complex(2, 3)
b = Complex(1 , -5)

print(a)
print(b)

print(a+b)
print(a*b)
print(a/b)