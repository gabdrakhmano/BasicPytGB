# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который
# результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня.

a = float(input('First day result: '))
b = float(input('Target result: '))
days = 1
while a < b:
    a *= 1.1
    days += 1
print(f'It will take {days} days to reach result of {b} km')
