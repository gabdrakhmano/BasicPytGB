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
