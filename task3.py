import random


def get_unique_list_numbers(start=-10, stop=10, size=15) -> list[int]:
  # TODO написать функцию для получения списка уникальных целых чисел
    if stop-start+1 < size:
        raise ValueError('size должен быть меньше stop-start+1')
    list_ = []
    while len(list_) < size:
        number = random.randint(start, stop)
        if number not in list_:
            list_.append(number)

    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
