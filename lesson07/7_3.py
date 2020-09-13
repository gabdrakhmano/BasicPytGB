# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В
# его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
# быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul(
# )), деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и целочисленное (с округлением до целого) деление клеток, соответственно. Сложение. Объединение двух
# клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток. Вычитание. Участвуют
# две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение. Умножение. Создается общая клетка из двух. Число ячеек общей клетки
# определяется как произведение количества ячеек этих двух клеток. Деление. Создается общая клетка из двух. Число
# ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток. В классе необходимо
# реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет
# организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
# между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются
# все оставшиеся. Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n**. Или, количество ячеек клетки равняется 15, количество ячеек в ряду —
# 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:
    nucleus: int

    def __init__(self, nucleus):
        if nucleus <= 0:
            raise ValueError(f'Argument should be positive integer, not {nucleus}')
        self.nucleus = nucleus

    def __add__(self, other):
        if type(other) != type(self):
            raise ValueError(f'{other} is {type(other)}, should be {type(self)}')
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        if type(other) != type(self):
            raise TypeError(f'{other} is {type(other)}, should be {type(self)}')
        if self.nucleus <= other.nucleus:
            raise ValueError(f'Can subscript only smaller cell from bigger one')
        return Cell(self.nucleus - other.nucleus)

    def __mul__(self, other):
        if type(other) != type(self):
            raise ValueError(f'{other} is {type(other)}, should be {type(self)}')
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        if type(other) != type(self):
            raise ValueError(f'{other} is {type(other)}, should be {type(self)}')
        return Cell(self.nucleus // other.nucleus)

    def make_order(self, nuc_qty: int):
        rows = self.nucleus // nuc_qty
        return ('*' * nuc_qty + '\n') * rows + '*' * (self.nucleus % nuc_qty)


x = Cell(5)
y = Cell(7)
z = x + y
print(type(z), z.nucleus)
z = y - x
print(type(z), z.nucleus)
z = x * y
print(type(z), z.nucleus)
z = y / x
print(type(z), z.nucleus)
print(Cell.make_order(x + y, 5))
