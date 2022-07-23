num = int(input('Nhập số bất kì:'))
num1 = int(input('Nhập số bất kì:'))
num2 = int(input('Nhập số bất kì:'))
num3 = int(input('Nhập số bất kì:'))


if num % 3 == 0 and num % 5 == 0:
    print(num, 'is divisible by 3 and 5')

if num1 % 3 == 0 and not(num1 % 5 == 0):
    print(num1, 'is divisible by 3')

if num2 % 5 == 0 and not(num2 % 3 == 0):
    print(num2, 'is divisible by 5')

if not(num3 % 3 == 0) and not(num3 % 5 == 0):
    print(num3, 'is not divisible by 3 and 5')