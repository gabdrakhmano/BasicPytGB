# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def my_func(lst):
    int_lst = []
    no_specials = True
    for i in lst:
        if i.isdigit():  # в условии не сказано что такое "специальный символ", поэтому это будет любое не число
            int_lst.append(int(i))
        else:
            no_specials = False
            break
    return [sum(int_lst), no_specials]


total_sum = 0
while True:
    lst = list(input('Enter few numbers separated by space: ').split(' '))
    lst_sum, go_on = my_func(lst)
    total_sum += lst_sum
    print(f'Total sum = {total_sum}')
    if not go_on:
        print(f'Quitting due to not a number')
        break
