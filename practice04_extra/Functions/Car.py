class Car:
    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year

    def get_info(self):
        return 'Name: {} \nPrice: {}\nYear: {}'.format(str(self.name),
                                                       str(self.price),
                                                       str(self.year))
