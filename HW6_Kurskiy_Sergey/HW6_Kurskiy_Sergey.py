# ------- task 1

print("\ntask1 \n")

import task1

task1.Light(5 , 6 , 4 , 1)

# ------ task 2

print("\ntask2 \n")

import  task2

task2.roads(4500 , 45 , 10)

# ------ task 3

print("\ntask3 \n")

import task3

worker = task3.Worker("test" , "test" , "IT_master" , 45000 )

worker_pos = task3.Position(worker)

worker_pos.get_full_name()
worker_pos.get_total_income()

# ------ task 4

print("\ntask4 \n")


import task4

police = task4.PoliceCar(70 , "blue" , "Lexus" , True)

police.show_info()
police.show_speed()
police.movement(2)

print("\n")
work_car = task4.WorkCar(50 , "black" , "Nissan")
work_car.show_speed()

# ----- task 5

print("\ntask5 \n")

import task5

shop_thing = task5.Stationery()

pen = task5.Pen("PEN")
pencil = task5.Pencil("PENCIL")
handle = task5.Handle("Handle")

shop_thing.draw()
pen.draw()
pencil.draw()
handle.draw()