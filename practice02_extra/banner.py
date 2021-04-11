import pyfiglet


# Способ №1
def method1(text):
    a = []
    i = 0

    with open('source/letters.txt') as file:
        lines1 = file.read()
        lines2 = lines1.split('@@')
    lines2.pop()

    for line in lines2:
        a.append(line.split('@\n'))
        if (a[i][0][:1] == "\n"):
            a[i][0] = a[i][0].replace('\n', '')
        i += 1

    for j in range(6):
        temp = ''
        for i in range(len(text)):
            Ind = ord(text[i])
            if (65 <= Ind <= 90):
                temp += a[Ind - 65][j]
            elif (97 <= Ind <= 122):
                temp += a[Ind - 71][j]
        print(temp)


# Способ №2
def method2(string):
    print(pyfiglet.figlet_format(string))


method1('University')
print('-------------------------------------------------------------------------------')
method2('Institute')
