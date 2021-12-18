#1
"""class Products:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f'"Naming"- {self.name}\n"Price"- {self.price} uah\n"Description"- {self.description}\n"Dimensions"- {self.dimensions}'




products = ["pan", "cups", "spoon", "fork"]
price = [200, 50, 40, 45]
description = ["China manufacturer made of aluminum", "Ceramic volume 0.5 milliliters", "set of 20", "set of 20"]
dimensions = ["10 x 5", "1 x 1", "2 x 2", " 2 x 2"]
x = Products(name=products[0], price=price[0], description=description[0], dimensions=dimensions[0])

for count in range(3):
    print(Products(name=products[count], price=price[count], description=description[count], dimensions=dimensions[count]), '\n')"""
#2
"""class Customer:
    def __init__(self, name, surname, number_phone):
        self.name = name
        self.surname = surname
        self.number_phone = number_phone
        
    def __str__(self):  
        return f'name - {self.name},surname - {self.surname},number_phone - {self.number_phone} '


user_1 = Customer("John", "Dennis", +358_44_9475_168)
print(user_1)
user_2 = Customer("Jordan", "Robbins", +371_24_827_505)
print(user_2)
user_3 = Customer("Leslie ", "Perkins", +372_546_9087)
print(user_3)"""
#3
class Order:

    class Customer:
        def __init__(self, name, surname, number_phone):
            self.name = name
            self.surname = surname
            self.number_phone = number_phone

        def __str__(self):
            return f'Hello {self.name}, an order has been made by your number {self.number_phone}'

    class Products:
        def __init__(self, choice, suma):

            self.choice = choice
            self.suma = suma

        def __str__(self):
            return f'You ordered {choice} for the amount {suma} grn'


import random
def choice(products):
    list = []
    choice = []
    for key, value in products.items():
        list_1 = [key, value]
        list.append(list_1)
    for r in range(0, random.randint(1, 4)):
        choice.append(list[random.randint(0, 3)])
    return choice

def sort(choice):
    selected_products = []
    sum = 0
    for elem in choice:
        for el in elem:
            if isinstance(el, int):
                sum += el
            else:
                selected_products.append(el)
    return selected_products, sum


products = {"pan": 200, "cups": 50, "spoon": 45, "fork": 40}
choice = choice(products)
choice, suma = sort(choice)
customer1 = Order.Customer("John", "Dennis", +358_44_9475_168)
print(customer1, Order.Products(choice, suma))



