
def custom_write (file_name, strings):

    text_file = file_name

    list_pos = [0]

    for i in strings:
        with open(text_file, 'a') as file:
            file.write(i + '\n')
            pos = file.tell()
            list_pos.append(pos)


    for i in range (len(strings)):
        strings_positions = {(i + 1, list_pos[i]) : strings[i]}
        print(*strings_positions.items())



print()

info = [
    'Text for tell.',
    'Используйте кодировку UTF-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]


result = custom_write('test.txt', info)






