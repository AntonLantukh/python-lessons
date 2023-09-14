"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(map(lambda x: x ** 2, args))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num <= 1:
        return False

    for n in range(num - 1, 1, -1):
        if (num % n == 0):
            return False

    return True


def filter_numbers(arr, type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    if (type == PRIME):
        return list(filter(is_prime, arr))
    elif (type == EVEN):
        return list(filter(lambda num: num % 2 == 0, arr))
    elif (type == ODD):
        return list(filter(lambda num: num % 2 != 0, arr))


print(filter_numbers([1, 2, 10, 22, 43, 71], 'prime'))
