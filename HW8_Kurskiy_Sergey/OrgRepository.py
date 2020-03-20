"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""
import datetime

class PriceExeption(Exception):
    info = "Price of the models is not equal"

    @staticmethod
    def price_check(device , new_device):
        if device.price != new_device.price:
            raise PriceExeption()

class DeviceExeption(Exception):
    info = "element_devices are not equal"

    @staticmethod
    def device_check(device, new_device):
        if device.element_device != new_device.element_device:
            raise DeviceExeption()

class Repository:

    database = {"Printer" : {} ,"Scaner" : {} }


    def to_take(self , device, amount=1):
        if isinstance(amount, int):
            type = str(device.__class__)[:-2].split(".")
            if Repository.database.get(type[1]) is None:
                new_device = {type[1] : {}}
                Repository.database.update(new_device)

            type_info = Repository.database.get(type[1])
            if type_info.get(device.model) is None:
                new_model = {device.model : [amount, device]}
                type_info.update(new_model)
            else:
                try:
                    count = type_info.get(device.model)
                    PriceExeption.price_check(count[1], device)
                    DeviceExeption.device_check(count[1], device)
                    type_info.update({device.model : [count[0] + amount, count[1]]})
                except PriceExeption:
                    print(PriceExeption.info)
                except DeviceExeption:
                    print(DeviceExeption.info)
        else:
            print("Amount need type of integer")

    def to_send(self, type, model, department, amount=1):
        if isinstance(amount, int):
            type = type.title()
            if Repository.database.get(type) is None:
                print("No such type of element")
            elif Repository.database.get(type).get(model) is None:
                print("No such model")
            else:
                element = Repository.database.get(type).get(model)
                with open("logs.txt" , "a", encoding='utf8') as file:
                    if element[0] - amount > 0:
                        Repository.database.get(type).update({model : [element[0] - amount, element[1]]})
                        file.write(f"Send {type} model - {model} in amount {amount} to {department} at {datetime.date.today()}\n")
                    else:
                        file.write(f"Send {type} model - {model} in amount {element[0]} to {department} at {datetime.date.today()}\n")
                        Repository.database.get(type).pop(model)
        else:
            print("Amount need type of integer")


    def repository_info(self):
        for el in Repository.database:
            print(f"\t\033[32m{el}\033[0m")
            info = Repository.database.get(el)
            if len(info) == 0:
                print("No such element")
            else:
                print("\033[4mModel - Amount\033[0m")
                for model in info:
                    print(f"\033[31m{model} - {info.get(model)[0]}\033[0m")
            print()

    def element_info(self, type, model):
        type = type.title()
        if Repository.database.get(type) is None:
            print("No such type of element")
        elif Repository.database.get(type).get(model) is None:
            print("No such model")
        else:
            Repository.database.get(type).get(model)[1].info

class Orgtech:
        mass = 25
        material = "plastic"

        @staticmethod
        def cur__type_discount(cls, new_discount):
            cls.discount = new_discount

class Printer(Orgtech):
    discount = 0

    def __init__(self, price, model, print_device="printer"):
        self.price = price
        self.model = model
        self.element_device = print_device

    @property
    def info(self):
        print(f"Printer\nmodel - {self.model}\nprice - {self.price}\ndiscount - {self.discount}%\nmass - {self.mass}\nmaterial - {self.material}\ndevice - {self.element_device}")


class Scaner(Orgtech):
    discount = 0

    def __init__(self, price, model, scan_device="scaner"):
        self.price = price
        self.model = model
        self.element_device = scan_device

    @property
    def info(self):
        print(
            f"Scaner\nmodel - {self.model}\nprice - {self.price}\ndiscount - {self.discount}%\nmass - {self.mass}\nmaterial - {self.material}\ndevice - {self.element_device}")


class Xerox(Orgtech):
    discount = 0

    def __init__(self,price, model, xerox_device="xerox"):
        self.price = price
        self.model = model
        self.element_device = xerox_device

    @property
    def info(self):
        print(
            f"Xerox\nmodel - {self.model}\nprice - {self.price}\ndiscount - {self.discount}%\nmass - {self.mass}\nmaterial - {self.material}\ndevice - {self.element_device}")



if __name__ == "__main__":

    # Создаем элементы
    printer = Printer(128, 'model-x0123')
    scaner = Scaner(100, 'scaner_model-s34Ts2')
    xerox = Xerox(10, 'xerox-ertGs289')

    # Менеяем параметры классов на нужные
    Orgtech.cur__type_discount(Printer, 10)
    Orgtech.cur__type_discount(Scaner, 5)
    Orgtech.cur__type_discount(Xerox, 15)

    # Создание склада
    rep = Repository()

    # Берем на склад элементы в определенном количестве
    rep.to_take(xerox, 20)
    rep.to_take(printer, 15)
    rep.to_take(scaner, 5)

    # Получаем информацию о складе
    rep.repository_info()

    # Получаем информацию о конкретном типе и модели этого типа
    rep.element_info('printer' , 'model-x0123')
    print()
    # Отправляем определенный тип и модель в магазин в определенном количестве
    rep.to_send('xerox' , 'xerox-ertGs289' , 'МВидео', 10)
    rep.to_send('printer', 'model' , 'Tech')
    print()
    rep.repository_info()