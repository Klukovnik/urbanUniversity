class House:

    def __init__(self):
        self.number_of_floors = []
    def setNewNumberOfFloor (self, floors):
        self.number_of_floors.append(floors)
        print('Едем на', floors, 'этаж')

print()
my_house = House()
my_house.setNewNumberOfFloor(floors=15)
my_house.setNewNumberOfFloor(floors=18)
my_house.setNewNumberOfFloor(floors=23)
