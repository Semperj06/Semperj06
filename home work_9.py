import time

def count(f):
    count = 0

    def count1(*args):
        nonlocal count
        count += 1
        return f"Number of times = {count}", f"Result = {f(*args)}"
    return count1


def register(func):
    list_of_func = {}
    count = 0

    def register1(*args, **kwargs):
        nonlocal count
        count += 1
        list_of_func[count] = func(*args, **kwargs)
        return func(*args, **kwargs)
    return register1


def record(cls):

    def record1(*args, **kwargs):
        file = open(cls + ".txt", "w")
        file.write(cls(*args, **kwargs))
        file.close()
    return record1

@count
@register
def sum(x, y):
    return x + y

#1)


def register(cls):
    class_list = []

    def register1(*args, **kwargs):
        class_list.append(cls)
        return f"{(cls(*args, **kwargs))}"
    return register1


def get_str(arg):
    def cl(cls):
        def retrn(*args):
            new_instance = str(cls(*args))
            return f"{arg}, {new_instance}"
        return retrn
    return cl




class MyDescription1:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, instance_class):
        return f"{self.value}"

    def __set__(self, instance, value):
        raise AttributeError("You cant do this")

    def __delete__(self, instance):
        raise AttributeError("You cant do this")

    def __str__(self):
        res = ""
        for item in self.__dict__:
            res += f" {item} - {str((self.__dict__[item]))}\n"
        return f"{res}"


class MyDescription:

    def __get__(self, instance, instance_class):
        p = (instance_class.a + instance_class.b + instance_class.c) / 2
        s = p * (p - instance_class.a) * (p - instance_class.b) * (p - instance_class.c)
        s = s ** 0.5
        instance.__dict__["area"] = s
        return f"Area = {s}"

    def __set__(self, instance, value):
        raise AttributeError("You cant do this")

    def __delete__(self, instance):
        raise AttributeError("You cant do this")


class Triangle:
    """Реализация в классе двух дескрипторов с помощью первого делаем поля класса управляемые и
доступными только для чтения второй высчитывает площадь на основе 3 сторон, поле так же только для чтения"""
    a = MyDescription1(3)
    b = MyDescription1(4)
    c = MyDescription1(5)
    area = MyDescription()

    def __str__(self):
        return f"Triangle has ben made"


class Box:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.v = self.volume()

    def volume(self):
        v = self.a * self.b * self.c
        return int(v)

    def add(self, other):
        if isinstance(other, Box):
            x = self.v + other.v
            return x

    def __getattr__(self, item):
        return item

    def __setattr__(self, key, value):
        if isinstance(value, int) and value > 0:
            text = open('Box.txt', 'a')
            self.__dict__[key] = value
            tm = time.ctime()
            text.write(f"{tm} - [{key}, {value}]\n")
            text.close()
        elif value <= 0:
            raise ZeroDivisionError("Number cannot ba negative")
        else:
            raise TypeError("Must be integer")

    def __delattr__(self, item):
        return None

    @get_str("Current box have this parameter")
    def __str__(self):
        return f"{self.a}, {self.b}, {self.c}"
