"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Data:
    day = 0
    mounth = 0
    year = 0
    def __init__(self , str_data):
        self.str_data = str_data
        Data.data_transform(str_data)

    @property
    def full_data(self):
        print(f"Input data - {self.str_data}\nCurrent data - {Data.day} day {Data.mounth} mounth {Data.year} year")

    @staticmethod
    def validation(day, mounth, year):
        if 1 <= day <= 31 and 1 <= mounth <= 12 and year > 0:
            return True
        return False

    @classmethod
    def data_transform(cls , str_data):
        data = str_data.split('-')
        if Data.validation(int(data[0]), int(data[1]), int(data[2])):
            cls.day = int(data[0])
            cls.mounth = int(data[1])
            cls.year = int(data[2])
        else:
            print("Wrong data")



if __name__ == "__main__":

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