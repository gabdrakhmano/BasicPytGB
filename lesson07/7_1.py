# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде. Далее реализовать
# перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом
# сложения должна быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    data: list

    def __init__(self, *lists):
        for lst in lists:
            if len(lists[0]) != len(lst):
                raise ValueError('Lists should have same length')
        self.data = [*lists]

    def __str__(self):
        output = ''
        for line in self.data:
            line_print = ' '.join(map(str, line))
            output += line_print + '\n'
        return output[:-1]

    def __add__(self, other):
        result = []
        if len(self.data) != len(other.data):
            raise ValueError('Two matrices must have an equal number of rows and columns to be added.')
        for row in range(len(self.data)):
            if len(self.data[row]) != len(other.data[row]):
                raise ValueError('Two matrices must have an equal number of rows and columns to be added.')
        for row in range(len(self.data)):
            res_line = []
            for col in range(len(self.data[0])):
                res_line.append(float(self.data[row][col]) + float(other.data[row][col]))
            result.append(res_line)
        return Matrix(*result)


matrix1 = Matrix([1, 2, 3], [4, 5, 6])
matrix2 = Matrix([11, 12, 13], [14, 15, 16])
print(matrix1)
print(matrix2)
x = matrix1 + matrix2
print(x)
