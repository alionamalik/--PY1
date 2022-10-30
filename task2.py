def get_count_char(str_):
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    char_dict = {}
    for char in str_.lower():
        if char.isalpha():
            char_dict[char] = char_dict.get(char, 0) + 1

    return char_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""


def get_percent_char():
    main_dict = get_count_char(main_str)
    total_number = sum(main_dict.values())
    for key, value in main_dict.items():
        main_dict[key] = round(value/total_number*100, 2)
    print('Проверка:')
    print('Всего процентов:', round(sum(main_dict.values())))
    return main_dict


print(get_count_char(main_str))     #первая функция
print(get_percent_char())       #вторая функция
