# class Rectangle:
#     def __init__(self, x, y, width, heigth):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.heigth = heigth
#
#     def __str__(self):
#         return f'Rectangle : {self.x}, {self.y}, {self.width}, {self.heigth}.'
#
#
# rect_1 = Rectangle(5, 10, 50, 100)
# print(rect_1)


# class Customers:
#     def __init__(self, first_name, second_name, city, balance):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.balance = balance
#         self.city = city
#
#     def __str__(self):
#         return f'''"{self.first_name} {self.second_name}". {self.city}. Баланс: {self.balance} руб.'''
#
#
# customer_1 = Customers('Иван', 'Петров', 'Москва', 50)
# print(customer_1)


class Customers:
    def __init__(self, first_name,second_name,city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.balance = balance
        self.city=city

    def __str__(self):
        return f'''"{self.first_name} {self.second_name}". {self.city}. Баланс: {self.balance} руб.'''

    def get_guest(self):
        return f'{self.first_name} {self.second_name},г. {self.city}'


costomer_1 = Customers('Иван','Петров','Москва',50)
costomer_2 = Customers('Владимир','Зайцев','Кострома',50)
costomer_3 = Customers('Олеся','Янина','Новосибирск',50)

guest_list=[costomer_1,costomer_2,costomer_3]


for guest in guest_list:
    print(guest.get_guest())

