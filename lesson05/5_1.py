# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.

try:
    with open('5_1.txt', 'w') as file:
        while True:
            line = input('Provide a line to write to file: ')
            if not line:
                break
            print(line, file=file)
except Exception as error:
    print(error)
