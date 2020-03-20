"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class ZeroDivision(Exception):

    def __init__(self, info = "Can`t divide on 0!"):
        ZeroDivision.info = info

def division():
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        if b == 0:
            raise ZeroDivision()
        else:
             res = a / b
    except ZeroDivision:
        print(ZeroDivision.info)
    else:
        print(f"a/b = {res}")