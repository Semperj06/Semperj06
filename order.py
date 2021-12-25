
class Custom_Excep(Exception):

    def __str__(self):
        return "The value cannot be negative"


class Customer:
    """Класс покупатель, состоит из имени фамилии и номера телефона """
    def __init__(self, name: str, surname: str, number_phone: int):
        self.name = name.title()
        self.surname = surname.title()
        self.number_phone = number_phone

    def __str__(self):
        return f'Hello {self.name}, an order has been made by your number {self.number_phone}'


class Products:
    """Класс продукты содержит в себе миксин цена и название продукта плюс описание и габориты """
    def __init__(self, name: str, price: (int | float), description: str, dimensions: str):
        if not isinstance(price, int | float):
            raise ValueError("Incorrect value")
        if price <= 0:
            raise Custom_Excep
        for elem in name:
            if elem.isdigit():
                raise ValueError("Incorrect value")
        self.price = price
        self.name = name.title()
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f'"Naming": {self.name}\n"Price": {self.price} uah\n"Description": {self.description} {self.dimensions}'


class Order:
    """Класс заказ использует класс  пользователь, параметр продукты принимает в себя список"""
    def __init__(self, customer: Customer, *product):
        self.customer = customer
        self.product = product
        self.shopping_basket = []
        for elem in product:
            self.shopping_basket.append(elem.name)

    def __str__(self):
        return f'{self.customer} \nYour order:{self.shopping_basket} \nAmount to pay: {self.sum()} grn'

    def sum(self):
        """Функция считает сумму списка продукты """
        suma = 0
        for s in self.product:
            print(s)
            suma += s.price
        return suma


if __name__ == "__main__":
    product_1 = Products("pan", -200.21, "China manufacturer made of aluminum", "10 x 5")
    product_2 = Products("cups", 20, "Ceramic volume 0.5 milliliters", "1 x 1")
    product_3 = Products("spoon", 45, "set of 20", "2 x 2")
    product_4 = Products("fork", 40, "set of 20", "2 x 2")
    customer_1 = Customer("John", "Dennis", +358_44_9475_168)
    customer_2 = Customer("Jordan", "Robbins", +371_24_827_505)
    order_1 = Order(customer_1, product_1, product_2, product_1)
    order_2 = Order(customer_2, product_3, product_4)
    print(product_1)

