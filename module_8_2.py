def personal_sum(numbers):

    result = 0
    incorrect_data = 0

    if type(numbers) == int:
        print('В numbers записан некорректный тип данных')

    else:

        for i in range(len(numbers)):

            try:
                result += numbers[i]

            except (TypeError):
                print('Некорректный тип данных для подсчёта суммы:', numbers[i])
                incorrect_data += i


        return (result, incorrect_data)




def calculate_average(numbers):

    if type(numbers) == int:
        print('В numbers записан некорректный тип данных')

    else:
        data_from_pers = personal_sum(numbers)

        try:
            average = data_from_pers[0] / len(numbers)
            return average

        except (ZeroDivisionError):
            print('0')

        except (TypeError):
            print('В numbers записан некорректный тип данных')










print(f'Результат 1: {calculate_average('1,2,3')}')
print()
print(f'Результат 2: {calculate_average([1, 'строка', 3, 'ещё строка'])}')
print()
print(f'Результат 3: {calculate_average(567)}')
print()
print(f'Результат 4: {calculate_average([42,15,36,13])}')