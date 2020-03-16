class Matrix:

    def __init__(self , *args):

        self.matrix = []
        self.column_count = 0
        self.row_count = len(args)
        for el in args:
            if len(el) > self.column_count:
                self.column_count = len(el)
            self.matrix.append(el)
        for row in self.matrix:
            if len(row) < self.column_count:
                for i in range(self.column_count - len(row)):
                    row.append(0)


    def __str__(self):

        result = ""
        for row in self.matrix:
            for el in row:
                result += f"{el}\t"
            result += "\n"

        return result


    def __add__(self, other):

        if self.column_count == other.column_count and self.row_count == other.row_count:

            new_matrix = Matrix([])
            for i in range(self.row_count):
                for j in range(self.column_count):
                    new_matrix.matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
                new_matrix.matrix.append([])
            return new_matrix
        else:
            return "Нельзя складывать матрицы разной размерности!\n"


if __name__ == "__main__":


    A = Matrix([2] , [3 , 6])
    B = Matrix([3 , 1] , [4 , 8])
    C = Matrix([3 , 0 , 1] , [2 , 1] , [3 , 2 , 5])
    D = Matrix([2 , 10 , 15] , [ 3 , 8 , 11] , [0 , 2 , 5])
    E = A + B
    F = C + D
    G = D + F

    print(A)
    print()
    print(B)
    print()
    print(C)
    print()
    print(D)
    print()
    print(E)
    print()
    print(F)
    print()
    print(G)