class House:
    def __init__(self):
        self.number_of_floors = 0

    def setNewNumbersOfFloors(self, floors = 10):
            self.number_of_floors = floors
            print(f'Вы приехали на {self.number_of_floors} этаж')

print()
my_house = House()
my_house.setNewNumbersOfFloors()

print()
my_house.setNewNumbersOfFloors(20)

print()
my_house.setNewNumbersOfFloors(5)


