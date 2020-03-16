class Cell:

    def __init__(self , cells_ammount):
        if cells_ammount >= 0:
            self.cells_ammount = cells_ammount
        else:
            return None

    def __add__(self, other):
        return Cell(self.cells_ammount + other.cells_ammount)

    def __sub__(self, other):
        if self.cells_ammount > other.cells_ammount:
            return Cell(self.cells_ammount - other.cells_ammount)
        return "Вычитание невозможно!\nВычитаемая клетка больше исходной\n"

    def __mul__(self, other):
        return Cell(self.cells_ammount * other.cells_ammount)

    def __truediv__(self, other):
        return Cell(self.cells_ammount // other.cells_ammount)
    # Не до конца понял какое деление( целочисленное или нет ) делать
    # Так как в начале задания и в конце написаны разные требования.
    # Но сделал челочисленное. Оно кажется более логичным с точки зрения органики

    def __str__(self):
        return f"number of cells - {self.cells_ammount}\n"

    def make_order(self , max_cells_in_row):
        result = ""
        rows = self.cells_ammount // max_cells_in_row
        extra_cells = self.cells_ammount % max_cells_in_row

        simple_str = ""
        for i in range(max_cells_in_row):
            simple_str += "*"
        simple_str +="\n"

        for i in range(rows):
            result += simple_str

        if extra_cells != 0:
            for i in range(extra_cells):
                result += "*"
            result +="\n"

        print(result)



if __name__ == "__main__":

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