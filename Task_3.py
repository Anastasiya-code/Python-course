x = float(input('Введите координату x: '))

y = float(input('Введите координату y: '))
while x == 0 and y == 0:
    print('Вы ввели некорректное число, x и y не могут равняться 0.')
    y = float(input('Введите координату y: '))
if x > 0 and y > 0:
    print(1)
elif x < 0 < y:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 > y:
    print(4)
elif x == 0:
    print('y')
else:
    print('x')