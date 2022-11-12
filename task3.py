import random


def get_unique_list_numbers() -> list[int]:
    list_ = [random.randint(-10, 10) for n in range(16)]  # TODO написать функцию для получения списка уникальных целых чисел
    while not len(list_) == len(set(list_)):
        list_ = [random.randint(-10, 10) for n in range(16)]
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
