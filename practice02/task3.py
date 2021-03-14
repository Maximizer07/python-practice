def f23(my_table):
    format_table = list()
    for i in range(len(my_table)):  # удаление пустых строк
        for j in range(len(my_table[i])):
            if my_table[i][j] is not None:
                format_table.append(my_table[i].copy())
                break

    my_table = format_table
    format_table = []
    first = True
    for i in range(len(my_table[0])):
        if my_table[0][i] is not None:
            for j in range(len(my_table)):
                if first:
                    format_table.append([my_table[j][i]])
                    if j == len(my_table) - 1:
                        first = False
                else:
                    format_table[j].append(my_table[j][i])

    my_table = format_table

    for line in my_table:  # преобразование
        for i in range(len(line)):
            if isinstance(line[i], str):
                if i == 0:
                    line[i] = float(line[i])
                    line[i] *= 10
                    line[i] = int(line[i] + (0.5 if line[i] > 0 else -0.5))
                    line[i] /= 10
                    line[i] = str(line[i])
                if i == 1:
                    line[i] = line[i][line[i].find("@")+1:]
                if i == 2:
                    line[i] = line[i][6:]
                    line[i] = line[i].replace("-", "")

    for i in range(len(my_table)-1):  # сортировка
        for j in range(len(my_table)-1-i):
            if my_table[j][2] and my_table[j+1][2] is not None:
                if int(my_table[j][2]) > int(my_table[j+1][2]):
                    my_table[j], my_table[j+1] = my_table[j+1], my_table[j]

    for line in my_table:
        print(line)

    return my_table


list1 = [None, None, None, None]
list2 = ['0.71', None, 'ciduzak78@rambler.ru', '(492) 514-7118']
list3 = [None, None, None, None]
list4 = ['0.56', None, 'sisij32@rambler.ru', '(368) 069-8185']
list5 = ['0.21', None, 'vladimir34@mail.ru', '(357) 357-0812']
list6 = ['0.73', None, 'muzokev10@rambler.ru', '(127) 650-4463']
a = [list1, list2, list3, list4, list5, list6]

list11 = [None, None, None, None]
list12 = ['0.71', None, 'rostislav64@gmail.com', '(929) 668-0795']
list13 = ['0.03', None, 'rofskij41@rambler.ru', '(612) 205-0103']
list14 = [None, None, None, None]
list15 = ['0.32', None, 'suluzberg51@mail.ru ', '(642) 860-3562']
b = [list11, list12, list13, list14, list15]

f23(a)
print("-----")
f23(b)
