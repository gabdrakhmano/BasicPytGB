a = float(input('First day result: '))
b = float(input('Target result: '))
days = 1
while a < b:
    a *= 1.1
    days += 1
print(f'It will take {days} days to reach result of {b} km')
