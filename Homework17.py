class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self, powers = 99):
        self.powers = powers
        if powers >= 100:
            self.price = 1000000 + (powers - 99) * 5000
            print('Стоимость автомобиля: ', self.price)
        else:
            print('Укажите мощность двигателя')

class Nissan(Car):
    pass

class Kia(Car):
    pass

print()
user_choice = int(input('Выберите марку автомобиля: \n - 1 Nissan \n - 2 Kia \n '))
if user_choice == 1:
    nissan = Nissan()
    nissan.horse_powers(150)
elif user_choice == 2:
    kia = Kia()
    kia.horse_powers(130)
else:
    print('Позвоните на Нашу горячую линию по номеру: +7 800 600 60 60')















