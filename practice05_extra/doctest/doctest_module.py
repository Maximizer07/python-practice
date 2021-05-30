import re


def p1(a: int, b: int, c: int) -> str:
    """
    Программа для тестирования 1.
    Установление по сторонам (a, b, c) треугольника его типа:
    равносторонний, разносторонний, равнобедренный.
    Примеры:
    >>> p1(2, 2, 2)
    'Равносторонний'
    >>> p1(3, 4, 5)
    'Разносторонний'
    >>> p1(2, 3, 2)
    'Равнобедренный'
    >>> p1(1, 2, -1)
    'Сторона не может быть меньше 0'
    >>> p1(1, 2, 1)
    'Такого треугольника не существует'

    :param a: сторона треугольника 1
    :param b: сторона треугольника 2
    :param c: сторона треугольника 3
    :return: тип треугольника
    """
    if a <= 0 or b <= 0 or c <= 0:
        return 'Сторона не может быть меньше 0'
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Такого треугольника не существует'
    if a == b == c:
        return 'Равносторонний'
    if a == b or a == c or b == c:
        return 'Равнобедренный'
    return 'Разносторонний'


def p2(password: str) -> bool:
    """
    Функция проверки пароля на безопасность (например: безопасный пароль
    содержит комбинирование шести или больше строчных и прописных букв,
    плюс знаки препинания и цифры).
    Примеры:
    >>> p2('123')
    False
    >>> p2('HelloGoodbye')
    False
    >>> p2('')
    False
    >>> p2('.Goodbye17?')
    True
    >>> p2('Goodbye17')
    False
    >>> p2('!goodbye17')
    False
    >>> p2('He15?')
    False

    :param password: пароль на проверку
    :return: результат проверки пароля
    """
    return bool(re.match(
        r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[.,;!?]).{6,}$',
        password))
