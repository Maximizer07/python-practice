import contextlib

"""
    Язык HTML-тегов с помощью менеджера контекста.
    Реализовать классы для выполнения примера.
"""


class Html:
    def __init__(self):
        self.data = ''

    @contextlib.contextmanager
    def body(self):
        elem = '<body>\n'
        self.data += elem
        try:
            yield
        except RuntimeError as err:
            print('error: ', err)
        finally:
            self.data += elem

    @contextlib.contextmanager
    def div(self):
        elem = '<div>\n'
        self.data += elem
        try:
            yield
        except RuntimeError as err:
            print('error: ', err)
        finally:
            self.data += elem

    def p(self, content):
        self.data += '<p>' + content + '</p>\n'

    def get_code(self):
        return self.data


html = Html()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')
print(html.get_code())
