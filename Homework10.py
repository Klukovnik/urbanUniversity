print()

def print_params_(a = 500, b = 'coconut milk', c = 10 > 9):
    print(a, b, c)

print_params_()
print()
print_params_(20, 200, 2000)

print()
print('вызов с разным количеством аргументов: ')
empty_box_1 = ''
empty_box_2 = ''
empty_box_3 = ''
print_params_(empty_box_1)
print_params_(empty_box_1, empty_box_2)

print()
print('вызов без аргументов: ')
print_params_(*['', '', ''])

print()
print_params_(b = 25)

print()
print_params_(c = [1, 2, 3])

print()
value_list = [5000, 50 > 60, 'juce']
value_dict = {'a' : 100, 'b' : 'coconut milk', 'c' : 10 > 9}

print_params_(*value_list)

print()
print_params_(**value_dict)

print()
value_list_2 = [100 == 100, 800]
print_params_(*value_list_2, 42)