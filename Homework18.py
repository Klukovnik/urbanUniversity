class Vehicle:
    def __init__(self):
        self.vehicle_type = 'none'

class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self, powers=100):
        self.powers = powers
        if powers >= 101:
            self.price = 1000000 + (powers - 100) * 5000
            print('Стоимость автомобиля: ', self.price)
        else:
            pass
class Nissan (Vehicle, Car):
    def __init__(self):
        super().__init__()
        super().horse_powers()
        self.vehicle_type = ['CrossRoad 4*4', 'Crossover Utility Vehicle', 'Pickup']


my_nissan = Nissan()
print()
print('Добро пожаловать на распродажу Nissan!!!')
print()
user_choice = int(input('Выберите модель автомобиля: \n - 1 Nissan Navara'
                        ' \n - 2 Nissan Murano \n - 3 Nissan X-Trail \n '))
if user_choice == 1:
    my_nissan.horse_powers(300)
    print(my_nissan.vehicle_type[2])
elif user_choice == 2:
    my_nissan.horse_powers(250)
    print(my_nissan.vehicle_type[0])
elif user_choice == 3:
    my_nissan.horse_powers(150)
    print(my_nissan.vehicle_type[1])
else:
    print('Позвоните на Нашу горячую линию по номеру: +7 800 600 60 60')







