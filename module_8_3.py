
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, __vin, __numbers):

        def is_valid_vin(__vin):

            if not isinstance(__vin, int):
                raise IncorrectVinNumber('Некорректный тип VIN номер')

            elif __vin < 1000000:
                raise IncorrectVinNumber('Неверный диапазон для VIN номера')

            elif __vin > 10000000:
                raise IncorrectVinNumber('Неверный диапазон для VIN номера')

            else:
                return True

        def is_valid_numbers(__numbers):

            if not isinstance(__numbers, str):
                raise IncorrectCarNumber('Некорректный тип данных для номеров')

            elif len(__numbers) != 6:
                raise IncorrectCarNumber('Неверная длина номера')

            else:
                return True

        self.model = model
        self.__vin = is_valid_vin(__vin)
        self.__numbers = is_valid_numbers(__numbers)


print()
try:
    first = Car('AUDI_A4', 1374568 , 'т001тр')

except IncorrectVinNumber as exc:
    print(exc.message)

except IncorrectCarNumber as exc:
    print(exc.message)

else:
    print(f'{first.model} успешно внесен в базу данных ГАИ')

print()

try:
    second = Car('AUDI_A4', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно внесен в базу данных ГАИ')

print()

try:
    third = Car('AUDI_A4', 2020002, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно внесен в базу данных ГАИ')







