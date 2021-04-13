import json
import requests
import csv
from yattag import Doc

letters = ['К', 'В', 'М', 'Н']
maxCount = [25, 13, 2, 10]
groups_id = {'К': -1, 'В': 24, 'М': 37, 'Н': 39}
task_id = {'f11': 1, 'f12': 2, 'f13': 3, 'f14': 4, 'f21': 5, 'f22': 6, 'f23': 7, 'f31': 8, 'C32': 9}
indent = ''
doc, tag, text = Doc().tagtext()
'''
K группы 0-24
В группы 25-34
Н группы 35-44
М группы 45-46
'''


def group_id(gr):
    x1 = gr[0]
    x2 = int(gr[1:])
    id = groups_id[x1] + x2
    return id


def indent_html(str, flag):
    if flag:
        str += '    '
    else:
        str = str[0:-4]
    return str


groups = [letters[i] + str(j + 1) for i in range(len(letters)) for j in range(maxCount[i])]
tables = [[['None' for i in range(10)] for j in range(41)] for k in range(50)]
for i, table in enumerate(tables):
    table[0][0] = 'Вариант'
    table[0][1] = '1.1'
    table[0][2] = '1.2'
    table[0][3] = '1.3'
    table[0][4] = '1.4'
    table[0][5] = '2.1'
    table[0][6] = '2.2'
    table[0][7] = '2.3'
    table[0][8] = '3.1'
    table[0][9] = '3.2'
    table[0].append(groups[i])
for table in tables:
    for i in range(1, 41):
        table[i][0] = str(i)

response = requests.get('http://sovietov.com/kispython/table.json')  # Get-запрос
json_data = json.loads(response.text)  # Извлекаем JSON
data = json_data['data']

for elem in data:
    if elem[2] in task_id:
        tables[group_id(elem[0])][elem[1]][task_id[elem[2]]] = elem[3]
tab = tables

with tag('html'):
    indent = indent_html(indent, 1)
    text('\n' + indent)
    with tag('body'):
        indent = indent_html(indent, 1)
        text('\n' + indent)
        for i in range(len(tables)):
            with tag('table'):
                indent = indent_html(indent, 1)
                text('\n' + indent)
                for j in range(len(tables[i])):
                    with tag('tr'):
                        indent = indent_html(indent, 1)
                        text('\n')
                        for k in range(len(tables[i][j])):
                            text(indent)
                            if j != 0:
                                with tag('td'):
                                    if tables[i][j][k] != 'None':
                                        text(f'{tables[i][j][k]}')
                                    else:
                                        text('')
                            else:
                                with tag('th'):
                                    if tables[i][j][k] != 'None':
                                        text(f'{tables[i][j][k]}')
                                    else:
                                        text('')
                            if k != len(tables[i][j]) - 1:
                                text('\n')
                        indent = indent_html(indent, 0)
                        text('\n' + indent)
                    if j == len(tables[i]) - 1:
                        indent = indent_html(indent, 0)
                    text('\n' + indent)
            if i == len(tables) - 1:
                indent = indent_html(indent, 0)
            text('\n' + indent)
    text('\n')

result = doc.getvalue()
# print(result)
fp = open('site.html', 'w', encoding="utf-8")
for s in doc.getvalue():
    fp.write(s)
fp.close()
# print("HTML complete")

myFile = open('tables.csv', 'w', newline='', encoding="utf-8")
with myFile:
    writer = csv.writer(myFile)
    for table in tables:
        writer.writerows(table)
# print("Writing complete")
