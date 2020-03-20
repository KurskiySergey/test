"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""

class ValueExeption(Exception):

    info = "Need digit not a string"

    @staticmethod
    def validation(value):
        try:
            int(value)
        except ValueError:
            raise ValueExeption()




def list_check():
    my_list = []

    while True:
        answer = input("Enter value or q to exit\n")
        try:
            if answer == "q":
                break
            else:
                ValueExeption.validation(answer)
                my_list.append(answer)
        except ValueExeption:
            print(f"{ValueExeption.info}")


    print(my_list)


if __name__ == "__main__":

    list_check()