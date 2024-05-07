class House:
    def __init__(self):
        self.number_of_floors = 10

print()
my_house = House()
for i in range(my_house.number_of_floors):
    if i == 0:
        print('Добро пожаловать в холл здания!')
    elif i <=8:
        print('Текущий этаж равен: ', i + 1)
    else:
        print('Крыша дома. Вход только персоналу здания.')
