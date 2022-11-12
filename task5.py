import random, string


def get_random_password(n=8) -> str:
    alphabet = string.ascii_uppercase+string.digits+string.ascii_lowercase
    password = ''.join(random.sample(alphabet, n))  # TODO написать функцию генерации случайных паролей
    return password


print(get_random_password())
