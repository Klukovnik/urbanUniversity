class House:
    def __init__(self, floors = 0):
        self.number_of_floors = floors

    def set_floors(self):
        if self.number_of_floors == 0:
            print('остаемся здесь?')
        else:
            print(f'едем на {self.number_of_floors} уровень')

print()
my_house = House(15)
my_house.set_floors()


print()
user_floors = int(input('на какой уровень Вам нужно? : '))
if user_floors < 1:
    print('Такого уровня нет в этом здании')
else:
    my_house = House(user_floors)
    my_house.set_floors()

print()
my_house = House()
my_house.set_floors()