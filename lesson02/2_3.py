# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

month = ''
while not month.isdigit() or int(month) not in range(1, 13):  # проверяем, что введено число и от 1 до 12
    month = input('Enter month number: ')
month = int(month)

m_list = [0, 'Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer',
          'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn', 'Winter']
print(m_list[month])

m_dict = {'Winter': [1, 2, 12], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
for item in m_dict.items():
    if month in item[1]:
        print(item[0])
