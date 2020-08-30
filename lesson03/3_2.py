# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def func(name, lastname, year, city, email, phone):
    print(f'{lastname} {name}, born {year}, living in {city}. Contacts: {email}, {phone}')


func(phone='+123123456', year=1965, city='Magadan', lastname='Magadanov', name='Ivan', email='vanya@magadan.ru')
