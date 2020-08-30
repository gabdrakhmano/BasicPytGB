# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень. ** Подсказка: ** попробуйте решить задачу
# двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без
# оператора **, предусматривающая использование цикла.


def my_func(a, b):
    return a ** b


def my_func2(a, b):
    sq = 1
    for i in range(abs(b)):
        sq *= a
    return 1 / sq


while True:
    try:
        x, y = float(input('Действительное положительное число x = ')), int(input('Целое отрицательное число y = '))
        if x > 0 > y:
            break
    except Exception:
        pass
    print('ERROR!!!11!!1 Try again!')
print(f'{x} ^ {y} = {my_func(x, y)}')
print(f'{x} ^ {y} = {my_func2(x, y)}')
