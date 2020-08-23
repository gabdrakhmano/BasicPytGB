# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и
# строк и сохраните в переменные, выведите на экран.

n = int(input('Age? '))
while True:
    if 0 < n < 130:
        break
    n = int(input('Acceptable values are from 0 to 130. Try again : '))
firstname = input('First name? ')
lastname = input('Last name? ')
print(f'{firstname} {lastname}, {n} years old')
