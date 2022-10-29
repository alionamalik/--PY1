def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    char_dict = {}
    CHAR_DEFAULT = 0
    str_.lower()
    for char in str_:
        if char.isalpha():
            char_dict[char] = char_dict.get(char, CHAR_DEFAULT) + 1
    sorted_chart_dict = dict(sorted(char_dict.items()))     #сортирую по алфавиту

    return sorted_chart_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

main_dict = get_count_char(main_str)     #создаю словарь для второй функции
def get_percent_char(dict_):
    total_number = sum(main_dict.values())
    TOTAL = 100
    new_values = []
    for value in main_dict.values():        #создаю список с процентами
        new_values.append(round(value/total_number*TOTAL, 2))
    i = 0
    while i < len(new_values):
        for key, value in main_dict.items():    #объединяю ключи из старого словаря с созданным списком
            main_dict[key] = new_values[i]
            i += 1
    print('Проверка:')
    print('Всего процентов:', round(sum(main_dict.values())))
    return main_dict


print(get_count_char(main_str)) #первая функция
print(get_percent_char(main_dict)) #вторая функция
