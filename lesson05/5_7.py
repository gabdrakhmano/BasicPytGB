# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.

from statistics import mean
import json

try:
    with open('5_7.txt', 'r') as file:
        lines = [line.split() for line in file]
        firms = {name: int(inc) - int(exp) for name, form, inc, exp in lines}
        av_profit = {"average_profit": mean([value for value in firms.values() if value > 0])}
        data = [firms, av_profit]
    with open("5_7.json", "w") as output:
        json.dump(data, output)
except Exception as error:
    print(error)
