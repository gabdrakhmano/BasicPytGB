# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

import re  # модуль функций с регулярными выражениями

try:
    with open('5_2.txt', 'r') as file:
        lines_list = [re.findall(r'\w+', line) for line in file]  # ищет и выдаёт список серии (+) из a-z A-Z 0-9 (\w)
        print(lines_list)
        lines_count = len(lines_list)
        words_count = sum(len(line) for line in lines_list)
        print(f'There are {lines_count} lines and {words_count} words in {file.name}')
except Exception as error:
    print(error)
