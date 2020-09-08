# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее
# 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
# подсчет средней величины дохода сотрудников. Пример файла:
#
# Иванов 23543.12
# Петров 13749.32
#
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

from statistics import mean

try:
    with open('5_3a.txt', 'r') as file:
        data = [line.split() for line in file]
        underpaid = [name for name, salary in data if float(salary) < 20000]
        average = mean(float(salary) for name, salary in data)
        print('Сотрудники с окладом менее 20 тыс: {}'.format(', '.join(underpaid)))
        print(f'Средняя ЗП: {average:.2f} рублей')
except Exception as error:
    print(error)

############################

try:
    with open('5_3b.txt', 'r') as file:
        rus = ('Ноль', 'Один', 'Два', 'Три', 'Четыре')
        data = [line.split(' — ') for line in file]  # убираем тире и создаём список [['One', '1\n'], ['Two', '2\n']...]
        new_data = [f'{rus[int(num)]} — {int(num)}' for eng, num in data]  # меняем англ на рус и добавляем тире обратно
    with open('5_3c.txt', 'w') as output:
        print(*new_data, sep='\n', file=output)
except Exception as error:
    print(error)
