"""
 Реализовать класс Stationery (канцелярская принадлежность).
 Определить в нем атрибут title (название) и метод draw (отрисовка).
 Метод выводит сообщение “Запуск отрисовки.”
 Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
 В каждом из классов реализовать переопределение метода draw.
 Для каждого из классов методы должен выводить уникальное сообщение.
 Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    def __init__(self , title = "unknown"):

        self.title = title

    def draw(self):
        print(f"Запуск отрисовки...")


class Pen(Stationery):

    def draw(self):
        print(f"This is \033[34m\033[3m{self.title}")
        Stationery.draw(Stationery)
        print("\033[0m" , end='')


class Pencil(Stationery):

    def draw(self):
        print(f"This is \033[2m{self.title}")
        Stationery.draw(Stationery)
        print("\033[0m", end='')

class Handle(Stationery):

    def draw(self):
        print(f"This is \033[31m\033[1m\033[4m{self.title}")
        Stationery.draw(Stationery)
        print("\033[0m", end='')



if __name__ == "__main__":

    shop_thing = Stationery()

    pen = Pen("PEN")
    pencil = Pencil("PENCIL")
    handle = Handle("Handle")

    shop_thing.draw()
    pen.draw()
    pencil.draw()
    handle.draw()
