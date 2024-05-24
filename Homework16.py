class Building:
    def __init__(self, floors, b_type = 'дерево'):
        self.number_of_floors = floors
        self.building_type = b_type

    def character(self):
        print(f'дом из {self.building_type} '
              f'с количеством {self.number_of_floors} этажей')

    def __eq__(self, other):
        return (self.number_of_floors == other.number_of_floors and
                self.building_type == other.building_type)


print()
house_1 = Building(5)

house_2 = Building(6, 'кирпич')

house_3 = Building(10, 'пено-бетон')

house_4 = Building(5)

house_1.character()
print()
house_2.character()
print()
house_3.character()
print()
house_4.character()
print()
print(house_1 == house_2)
print()
print(house_1 == house_3)
print()
print(house_1 == house_4)