"""
3. Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker:
    def __init__(self , name , surname , position , income , bonus = 200):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"income" : income , "bonus" : bonus}

class Position(Worker):

    def __init__(self , worker):
        Worker.name = worker.name
        Worker.surname = worker.surname
        Worker.position = worker.position
        Worker._income = worker._income

    def get_full_name(self):

        print(f"name : {Worker.name} , surname : {Worker.surname}")

    def get_total_income(self):

        profit = Worker._income.get("income") + Worker._income.get("bonus")

        print(f"Total profit = {profit}")


if __name__ == "__main__":

    worker =  Worker("Firstname" , "Lastname" , "sientist" , 2000 )
    worker_position = Position(worker)


    worker_position.get_full_name()
    worker_position.get_total_income()

