
# ------- task 1

print("\n task 1\n")

from MatrixOp import Matrix

A = Matrix([1] , [2 , 3])
B = Matrix([3])
C = Matrix([2] , [3 , 4])

print(f"A = \n{A}\n")
print(f"B = \n{B}\n")
print(f"C = \n{C}\n")
print(f"A + B = \n{A + B}\n")
print(f"A + C = \n{A + C}\n")

# -------- task 2

print("\n task 2\n")

from ClothFabric import *

suit = Suit(20)
print(suit.name)
suit.consumption()
suit.name = "Coat"
print(suit.name)


coat = Coat(25)
print(coat.name)
coat.consumption()
coat.name = "Suit"
print(coat.name)

cloth_fabric.fabric_info
cloth_fabric.total_consumption()

# -------- task 3

print("\n task 3\n")


from Cells import Cell

ch_1 = Cell(20)
ch_2 = Cell(35)
print(f"ch_1 + ch_2 = {ch_1 + ch_2}")
print(f"ch_1 - ch_2 = {ch_1 - ch_2}")
print(f"ch_2 - ch_1 = {ch_2 - ch_1}")
print(f"ch_1 * ch_2 = {ch_1 * ch_2}")
print(f"ch_1 / ch_2 = {ch_1 / ch_2}")
print(f"ch_2 / ch_1 = {ch_2 / ch_1}")

ch_1.make_order(5)
ch_1.make_order(6)