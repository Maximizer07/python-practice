import random


# Преобразовать элементы списка s из строковой в числовую форму.
def tostring(a):
    return [int(x) for x in a]


# Подсчитать количество различных элементов в последовательности s.
def num_of_diff_elem(s):
    return len(set(s))


# Обратить последовательность s без использования функций.
def custom_reverse(s):
    return s[::-1]


# Выдать список индексов, на которых найден элемент x в последовательности s.
def list_of_index(a, x):
    return [i for i in range(len(a)) if a[i] == x]


# Сложить элементы списка s с четными индексами.
def sum_even_indexes(s):
    return sum([s[i] for i in range(len(s)) if i % 2 == 0])


# Найти строку максимальной длины в списке строк s.
def max_len_list(s):
    return max([len(i) for i in s])


names = ['Александр', 'Дмитрий', 'Максим', 'Сергей', 'Андрей', 'Алексей', 'Илья', 'Кирилл', 'Михаил', 'Никита',
         'Матвей', 'Роман', 'Егор', 'Арсений', 'Иван', 'Денис', 'Евгений', 'Тимофей', 'Владислав', 'Игорь',
         'Владимир', 'Павел', 'Руслан', 'Марк', 'Константин', 'Тимур', 'Олег', 'Ярослав', 'Антон', 'Николай']
ignore = ['Ю', 'Ь', 'Ъ', 'Й', 'Ё', 'Ы']
alphabet = [chr(x) for x in range(ord('А'), ord('Я') + 1) if chr(x) not in ignore]
end_of_lastname = ['ов', 'ев', 'ин', 'ын', 'ский', 'цкий', 'ской', 'цкой', 'ой', 'ий', 'енков', 'их', 'ых', 'ко']
consonant_letters = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
vowel_letters = ['а', 'я', 'о', 'е', 'у', 'ю', 'ы', 'и', 'э', 'е']


# Реализуйте генератор случайных данных ФИО. Список распространенных имен позволяется скачать из интернета.
# Фамилии необходимо генерировать самостоятельно
def generate_fio():
    s = random.choice(names) + " " + random.choice(alphabet) + ". "
    for i in range(random.randint(1, 3)):
        if i == 0:
            s += random.choice(consonant_letters).upper()
        else:
            s += random.choice(consonant_letters)
        s += random.choice(vowel_letters)
    s = s + random.choice(consonant_letters) + random.choice(end_of_lastname)
    return print(s)


def report():
    part1 = ('Коллеги,', 'В то же время,', 'Однако,', 'Тем не менее,', 'Следовательно,', 'Соответственно,',
             'Вместе с тем,', 'С другой стороны,')
    part2 = ('парадигма цифровой экономики', 'контeкст цифровой трансформации', 'диджитализация бизнeс-процессов',
             'прагматичный подход к цифровым платформам', 'совокупность сквозных тeхнологий',
             'программа прорывных исслeдований', 'ускорeниe блокчeйн-транзакций', 'экспоненциальный рост Big Data')
    part3 = ["открывает новые возможности для", "выдвигает новые требования", "несёт в себе риски",
             "расширяет горизонты", "заставляет искать варианты",
             "не оставляет шанса для", "повышает вероятность", "обостряет проблему"]
    part4 = ["дальнейшего углубления", "бюджетного финансирования", "синергетического эффекта",
             "компрометации конфиденциальных", "универсальной коммодитизации",
             "несанкционированной кастомизации", "нормативного регулирования", "практического применения"]
    part5 = ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.",
             "опасных экспериментов.", "государственно-частных партнёрств.",
             "цифровых следов граждан.", "нежелательных последствий.", "внезапных открытий."]
    return random.choice(part1) + " " + random.choice(part2) + " " + random.choice(part3) + " " + random.choice(
        part4) + " " + random.choice(part5)


def groups():
    letters = ['K', 'В', 'Н']
    maxCount = [25, 13, 10]
    return [letters[i] + str(j + 1) for i in range(len(letters)) for j in range(maxCount[i])]


print(tostring(['1', '2', '3', '4', '5']))
print(num_of_diff_elem(['lol', 'kek', 'lol', 'yes', 'no', 'no', 'u']))
print(custom_reverse(['1', '2', '3', '4', '5']))
print(list_of_index(['1', '8', '1', '456', '1', '67', '21'], '1'))
print(sum_even_indexes([10, 999, 10, 999, 10]))
print(max_len_list(["test", "teeest", "teest", "teeest", "teeeest"]))
[generate_fio() for i in range(5)]
print(report())
print(groups())
