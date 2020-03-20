"""
 Реализовать проект «Операции с комплексными числами».
 Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
 Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
 Проверьте корректность полученного результата.
"""
import math

class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def length_2(self):
        return self.re * self.re + self.im * self.im

    def reverse(self):
        self.im = -self.im
        return self

    def __str__(self):
        if self.im >= 0:
            return f"{self.re} + {self.im}i"
        return  f"{self.re} - {abs(self.im)}i"

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __truediv__(self, other):
        c = self * other.reverse()
        length = other.length_2()
        c.re = c.re/length
        c.im = c.im/length
        other.reverse()
        return c





if __name__ == "__main__":

    a = Complex(2, 3)
    b = Complex(1 , -5)

    print(a)
    print(b)

    print(a+b)
    print(a*b)
    print(a/b)

