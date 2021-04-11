import re

bad_subj = ['main.py', 'k17 14', 'K13 18', 'к02 1', 'ИВБО-11 Вариант№14', 'к02 21', '1.3.py',
            'В 11 4', '\ufeff\u200b\u200bк20 21', 'B7 21', 'Фамилия Имя Задача 1.1', 'В03 12',
            'к08 24', 'к07 23', '1.2.py, 1.3.py, 1.4.py', '1.1.py', 'K14 23', 'в7 ', 'к6 ',
            '\u200b\u200bк20 21', 'к2 в3', 'В104', 'В1013', 'B3 29', 'v10 15', 'k13 30',
            'В 7 10', 'Фамилия И.О. к7 31', '1.2.py', 'К10', 'ПитонН4 н11', 'K13 28', 'К4',
            'K17 10', 'и4 11', 'Н1', 'н01 28', 'б3 5', 'Re: в6 28', 'к-11 3', '2_1.py, 2_2.py', 'в099', 'в0920',
            'в0942',
            'в4567']
dict = {'k': 'к', 'v': 'в', 'b': 'в', 'h': 'н', 'икбо': 'к', 'ивбо': 'в', 'инбо': 'н', 'б': 'в', 'вариант': ''}
new_subj = []


def parse_subj(text):
    text = text.lower()
    for elem in dict:
        if text.find(elem) != -1:
            text = text.replace(elem, dict.get(elem))

    text = re.sub("[^а-я0-9\\s]", "", text)
    text = re.sub("\\s+", " ", text)
    text = re.sub(r"\b[а-я]{2,}[0-9]*\b", ' ', text)

    text = text.strip()

    list1 = re.findall("[а-я]\\s+[0-9]", text)
    for el in list1:
        el = el.replace(' ', '')
        text = re.sub("[а-я]\\s+[0-9]", el, text)

    list2 = re.findall("[а-я][0-9]{3,}", text)
    for el in list2:
        if el[1] == '0':
            if int(text[3:]) > 40:
                text = ''
                continue
            text = text[0] + text[2] + ' ' + text[3:]

        else:
            if len(text[1:]) == 4:
                if int(text[1:3]) > 40 and int(text[3:]) > 40:
                    text = ''
                    continue

            text = text[0:3] + ' ' + text[3:]

    list0 = re.findall("[а-я]0+", text)
    for el in list0:
        t = el.find(el)
        if t + 1 < len(text):
            text = text[:t + 1] + text[t + 2:]

    list3 = re.findall(r'[а-я][0-9]+\s[а-я][0-9]+', text)
    for el in list3:
        t = el.find(' ')
        text = text[:t + 1] + text[t + 2:]
    return text


def result():
    for j in range(len(bad_subj)):
        if re.search('[а-я][0-9]+\\s[0-9]+', bad_subj[j]):
            new_subj.append(bad_subj[j])
        else:
            new_subj.append('INVALID')


print(bad_subj)
for i in range(len(bad_subj)):
    bad_subj[i] = parse_subj(bad_subj[i])
result()
print(new_subj)
for i in range(len(new_subj)):
    print(bad_subj[i], ' - ', new_subj[i])
