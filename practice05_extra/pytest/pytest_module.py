import re

import pytest


class Program:
    def __init__(self, func):
        self.func = func

    def invoke(self, param):
        return self.func(param)


@pytest.fixture
def program_2():
    p = Program(p2)
    return p


@pytest.fixture
def program_3():
    p = Program(p3)
    return p


@pytest.mark.parametrize('prop,res', [
    (',?Goodbye123', True),
    ('!goodbye17,15', False),
    ('Goodbye17,15', True),
    ('gg17?', False),
    ('123', False),
    ('HelloGoodbye', False),
    ('', False)
])
def test_p2(program_2, prop, res):
    assert program_2.invoke(prop) is res


@pytest.mark.parametrize('prop,res', [
    ('0.0.0.1', True),
    ('128.164.23.1', True),
    ('255.255.255.255', True),
    ('15.127.256.9', False),
    ('12764.231.18', False),
    ('lol.kek.lol.kek', False),
    ('a.b.c.d', False),
    ('', False)
])
def test_p3(program_3, prop, res):
    assert program_3.invoke(prop) is res


def p2(password: str) -> bool:
    """
    Функция проверки пароля на безопасность (например: безопасный пароль
    содержит комбинирование шести или больше строчных и прописных букв,
    плюс знаки препинания и цифры).
    """
    return bool(re.match(
        r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[.,;!?]).{6,}$',
        password))


def p3(ipv4: str) -> bool:
    """
    Проверка IPv4-адреса на корректность.
    """
    return bool(re.match(
        r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b',
        ipv4))
