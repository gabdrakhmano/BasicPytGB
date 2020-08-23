# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

# version 1
n = int(input('Enter n: '))
digits = 0
max_digit = 0
while True:
    if n // (10 ** digits) == 0:
        break
    digits += 1
while digits > 0:
    if max_digit < (n % (10 ** digits)) // (10 ** (digits - 1)):
        max_digit = (n % (10 ** digits)) // (10 ** (digits - 1))
    else:
        digits -= 1
print(f'Max digit in {n} is {max_digit}')

# version 2 (не уверен соответствует ли условию "используйте цикл while и арифметические операции")
n = int(input('Enter n: '))
max_digit = 9
while str(max_digit) not in str(n):
    max_digit -= 1
print(f'Max digit in {n} is {max_digit}')
