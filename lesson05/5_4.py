# 4. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import random

try:
    with open('5_4.txt', 'w') as output:
        data = [int(random() * 100) for i in range(5)]  # создание списка из 5 случайных чисел
        print(*data, sep=' ', file=output)  # запись в файл через пробел
    with open('5_4.txt', 'r') as file:  # из условия не понятно нужно ли читать данные из файла, но будем считать что да
        data = [int(num) for num in file.readline().split()]  # чтение из файла в список чисел
        print(sum(data))
except Exception as error:
    print(error)
