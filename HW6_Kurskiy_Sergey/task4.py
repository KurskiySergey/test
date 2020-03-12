"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""
from random import  randint
from time import sleep

class Car:

    def __init__(self , speed , color , name , is_police = False):

        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} is moving")

    def stop(self):
        print(f"{self.name} is stopped")

    def turn(self , direction):

        if direction == "right":
            print("Turn to the right")
        elif direction == "left":
            print("Turn to the left")
        elif direction == "back":
            print("Turn around")
        else:
            print("No turn")

    def show_speed(self):
        print(f"Current speed of {self.name} = {self.speed}")

    def show_info(self):
        print(f"name : {self.name} \n color : {self.color} \n is_police : {self.is_police}")

    def movement(self , max_movements = 0):

        movement_count = 0
        direction = ["right", "left", "back", "forward"]
        self.go()

        while True:
            delay = randint(3, 10)
            next_dir = direction[randint(0, len(direction)-1)]
            sleep(delay)
            self.turn(next_dir)

            if movement_count == max_movements-1:
                break

            movement_count += 1


        self.stop()




class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"Attention! speed is more then 60\n Current speed of {self.name} = {self.speed}")
        else:
            print(f"Current speed of {self.name} = {self.speed}")


class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f"Attention! speed is more then 40\nCurrent speed of {self.name} = {self.speed}")
        else:
            print(f"Current speed of {self.name} = {self.speed}")

class PoliceCar(Car):
    pass




if __name__ == "__main__":

    test_car = TownCar( 65 , "green" , "Nissan")

    test_car.show_info()
    test_car.show_speed()
    test_car.movement(5)