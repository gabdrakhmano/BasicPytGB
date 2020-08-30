# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.


def my_func(x, y, z):
    lst = [x, y, z]
    lst.remove(min(lst))
    return sum(lst)


print(my_func(2, 2, 8))
