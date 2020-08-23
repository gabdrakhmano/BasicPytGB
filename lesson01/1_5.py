# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.\

sales = float(input('Sales: '))
expenses = float(input('Expenses: '))
if sales > expenses:
    profit = sales - expenses
    print(f'Company is profitable. Profit is {profit:.2f}')
    print(f'Return on sales (ROS) is {profit / sales:.0%}')
    emp_qty = int(input('Employee quantity: '))
    print(f'Profit per employee is {profit / emp_qty:.2f}')
else:
    print(f'Company is unprofitable. Loss is {expenses - sales:.2f}')
