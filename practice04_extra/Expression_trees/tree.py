"""
   Работа с деревьями выражений
   1. Реализовать классы Num, Add, Mul.
   2. Реализовать класс-посетитель PrintVisitor для печати выражения.
   Обойтись без операторов ветвления.
   3. Реализовать класс-посетитель CalcVisitor для вычисления выражения.
   Обойтись без операторов ветвления.
   4. Реализовать класс-посетитель StackVisitor для порождения кода стековой
   машины по выражению. Обойтись без операторов ветвления.
   5. Добавьте классы Sub и Mul. В существующий код можно только добавлять
   новые строки, не изменяя старой части.
"""


class Num:
    def __init__(self, digit):
        self.digit = digit

    def stack(self):
        print('PUSH ' + str(self.digit))

    def __repr__(self):
        return str(self.digit)


class Operation:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


class Add(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
        self.digit = int(self.num1.digit + self.num2.digit)

    def count(self):
        return self.digit

    def stack(self):
        self.num1.stack()
        self.num2.stack()
        print('ADD')

    def __repr__(self):
        return '({} + {})'.format(self.num1, self.num2)


class Mul(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
        self.digit = int(self.num1.digit * self.num2.digit)

    def count(self):
        return self.digit

    def stack(self):
        self.num1.stack()
        self.num2.stack()
        print('MUL')

    def __repr__(self):
        return '({} * {})'.format(self.num1, self.num2)


class Sub(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
        self.digit = int(self.num1.digit - self.num2.digit)

    def count(self):
        return self.digit

    def stack(self):
        self.num1.stack()
        self.num2.stack()
        print('SUB')

    def repr(self):
        return '({} - {})'.format(self.num1, self.num2)


class CalcVisitor:
    def visit(self, expression):
        return expression.count()


class PrintVisitor:
    def visit(self, expression):
        return expression


class StackVisitor:
    def visit(self, expression):
        expression.stack()


ast = Add(Num(7), Mul(Add(Num(3), Num(6)), Num(2)))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
sv.visit(ast)
