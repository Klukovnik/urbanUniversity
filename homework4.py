print()
print('кортеж')
print()
immutable_var = 4000, 'pencil', 'apple', 10 > 5, 'Denis', ['10.01.2004', 'nut'], 250 + 250
print(immutable_var)
print()

# если один из элементов кортежа - список [1, 2, 3] то можно изменить элементы этого списка

immutable_var[5][1] = 'juce'
print(immutable_var)
print()

# можно изменить кортеж операцией умножения

print(immutable_var * 2)

# в других случаях кортеж - неизменямый объект
print()

print('список')
print()
mutable_list = [4000, 'pencil', 'apple', 10 > 5, 'Denis', '10.01.2004', 250 + 250]
print(mutable_list)
print()

mutable_list.remove('apple')
mutable_list.append(500 * 5)
mutable_list[0] = 80000
mutable_list[3] = 'Sveta'
mutable_list.extend(['apple', 'Kolya'])
print(mutable_list)