def test_function():
    print()
    def inner_function():
        print('Я в области видимости test_function')

    inner_function()



test_function()

# вызвать inner_function() в других случаях не получится; не "хватает" области видимости

