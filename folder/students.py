import human


class Student(human.Human):
    """Создаем под класс студент на основе класса человек, добавляем такие параметры как возраст и факультет"""
    def __init__(self, name, surname, date_birth, mobile_phone: int, faculty="math"):
        super().__init__(name, surname, date_birth)
        self.faculty = faculty
        self.mobile_phone = mobile_phone

    def __str__(self):
        res = super().__str__()
        return f'{res}'  '\n'f'faculty: {self.faculty}' '\n'f'mobile phone: {self.mobile_phone}'




oleh = Student("Oleh", "Olehov", 1998, 7657657)
ivanov = Student("Ivan", "Ivanov", 2000, 7657657657)
petrov = Student("Petr", "Petrov", 1999, 7657657657)
alexandr = Student("Alexandr", "Alex", 1995, 32132133)