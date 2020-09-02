# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary(hours: float, rate: float, bonus: float = 0):
    return (hours * rate) + bonus


hours, rate, bonus = float(argv[1]), float(argv[2]), float(argv[3])
print(salary(hours, rate, bonus))
