from practice04_extra.Functions.Car import Car

"""
    Напишите код, который выведет на экране все переменные объекта
    произвольного пользовательского класса.
"""
car = Car('BMW', 250000, 2001)
print(dir(car))
print(vars(car))
print(car.__dict__)
"""
    Напишите код, который по имени метода, заданному строкой, вызовет этот
    метод в некотором пользовательском классе.
"""
print('-----')
car = Car('BMW', 250000, 2001)
method_to_invoke = getattr(car, 'get_info')
print(method_to_invoke())
