print()
automobile = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
car_count = 0
for i in range(len(automobile)):
    print('Я езжу на автомобиле', automobile[i])
    car_count += 10 + len(automobile[i])
    print(car_count)