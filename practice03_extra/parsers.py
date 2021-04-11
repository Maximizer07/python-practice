import json
import email.utils
import re
import matplotlib.pyplot as plt
from practice02_extra.parser_kispython import tab

week_days_id = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
letters = ['к', 'в', 'м', 'н']
maxCount = [25, 13, 2, 10]
tasks = ['1.1', '1.2', '1.3', '1.4', '2.1', '2.1', '2.3', '3.1', '3.2']
tasks_result = [0 for i in range(9)]
groups = [letters[i] + str(j + 1) for i in range(len(letters)) for j in range(maxCount[i])]
erors = ['Invalid\nlist', 'Invalid\nnumber', 'Result is a string,\nnot a number', 'Syntax\neror']
erors_count = [0, 0, 0, 0]
frequency_day = [0 for i in range(24)]
frequency_week = [0 for j in range(7)]
mes_groups = [0 for j in range(50)]
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


#
def pr_sol(lst, index):
    res1 = sum([lst[i] for i in range(len(lst)) if isinstance(lst[i], int)])
    solution_tasks[index] += res1
    lst = lst[1:]
    for i in range(len(lst)):
        tasks_result[i] += lst[i] if isinstance(lst[i], int) else 0
    pass


# Получение укороченной строки дня недели
def week(s):
    return week_days_id[s[:3]]


# Получение порядкового номера группы
def group(s):
    return groups.index(s[:3].lower().strip())


# Подсчет ошибок
def count_eror(lst):
    if lst[0] is None:
        erors_count[1] += 1
        return
    elif len(lst[0]) == 0:
        if re.match(r'^-?\d+(?:\.\d+)$', lst[1]):
            erors_count[1] += 1
        else:
            erors_count[0] += 1
    elif re.match(r'^-?\d+(?:\.\d+)$', lst[0]):
        erors_count[1] += 1
        return
    elif lst[0][0] == '[':
        erors_count[0] += 1
        return
    elif not re.sub(r'\'[\w]+\'', '', lst[0]):
        erors_count[2] += 1
        return
    elif re.sub(r'\'?(\s*[-+]?(\d+(?:\.\d*)?|\.\d+)([eE][-+]?\d+)?|[0x][\d]+\s*)\'?', '',
                lst[0]) == '' or lst[0][0] == '(' or lst[0] == 'None':
        erors_count[2] += 1
        return
    else:
        erors_count[3] += 1


with open('source/table.json', encoding='utf8') as f:
    table = json.loads(f.read())  # Таблица решений задач

with open('source/failed.json', encoding='utf8') as f:
    failed = json.loads(f.read())  # Данные по ошибкам

with open('source/messages.json', encoding='utf8') as f:
    messages = json.loads(f.read())  # Полученные сообщения
messages_week = messages

# ПОдсчет активности студентов по дням и времени суток и в каких группах было отправлено больше всего сообщений
messages = [(m['subj'].upper(), email.utils.parsedate(m['date'])) for m in messages]
for msg in messages_week:
    frequency_week[week(msg['date'])] += 1
    mes_groups[group(msg['subj'])] += 1
for msg in messages:
    frequency_day[msg[1][3]] += 1

# Парная реверсивная сортировка топ10
top_msg = zip(mes_groups, groups)
top10_msg = sorted(top_msg, key=lambda tup: tup[0], reverse=True)
mes_groups_top = [top[0] for top in top10_msg][:10]
groups_top = [top[1] for top in top10_msg][:10]

# Подсчет решенных задач
solution_tasks = [0 for i in range(50)]
for i in range(len(tab)):
    for j in range(1, len(tab[i])):
        pr_sol(tab[i][j], i)

# Парная реверсивная сортировка топ10
top_right = zip(solution_tasks, groups)
top10_right = sorted(top_right, key=lambda tup: tup[0], reverse=True)
right_groups_top = [top[0] for top in top10_right][:10]
right_top = [top[1] for top in top10_right][:10]

# Проход по списку ошибок для подсчета
for el in failed:
    count_eror(failed[el])

plt.figure(1)
plt.title('Активность студентов по времени суток')
plt.ylabel('Количество сообщений')
plt.xlabel('Час дня')
plt.plot([str(i) for i in range(24)], frequency_day)

plt.figure(2)
plt.title('Активность студентов по дням недели')
plt.ylabel('Количество сообщений')
plt.bar(week_days, frequency_week)

plt.figure(3)
plt.title('В каких группах было отправлено больше всего сообщений')
plt.ylabel('Количество сообщений')
plt.xlabel('Учебная группа')
plt.bar(groups_top, mes_groups_top)

plt.figure(4)
plt.title('В каких группах было получено больше всего правильных решений')
plt.ylabel('Количество верных решений')
plt.xlabel('Учебная группа')
plt.bar(right_top, right_groups_top)

plt.figure(5)
plt.title('Какие задачи оказались самыми легкими, самыми сложными')
plt.ylabel('Количество верных решений')
plt.xlabel('Номер задания')
plt.bar(tasks, tasks_result)

plt.figure(6)
plt.title('Какие распространенные ошибки совершали студенты')
plt.ylabel('Количество ошибок')
plt.bar(erors, erors_count)
plt.show()
