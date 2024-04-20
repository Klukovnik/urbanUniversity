print()
def test_fruit_box_(*args, **value):
    print(args, value)

test_fruit_box_(120, 150, 210, 300, 430, 300 < 400,
                fruit_1 = 'banana', fruit_2 = 'kiwi', fruit_3 = 'cherry',
                fruit_4 = 'pear', fruit_5 = 'granat')



print()
def factorial_(n = 6):
    if n == 1:
        print('Факториал числа 6 = ', end = '')
        return 1
    else:
        return n * factorial_(n - 1)

print(factorial_())

#   либо другой вариант:

print()
def factorial_(n):
    if n == 1:
        print('Факториал числа = ', end = '')
        return 1
    else:
        return n * factorial_(n - 1)

param = int (input('Введите число для расчёта факториала: '))

if param < 0:
    print('для чисел меньше нуля факториал не расчитать (')

else:
    print(factorial_(param))

