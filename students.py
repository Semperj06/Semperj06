MAX_STUDENTS = 10


class Custom_Excep(Exception):
    def __str__(self):
        return "The group should not exceed 10 students or such a student has already been added to the group"



class Human:
    """Описываем человека его имя, фамилия, год рождения и отчество если есть"""
    def __init__(self, name: str, surname: str, date_birth: int):
        self.name = name
        self.surname = surname
        self.date_birth = date_birth

    def __str__(self):
        return f'{self.name} {self.surname[0]}.' '\n'f'Age: {self.age()} date of birth: {self.date_birth}'

    def age(self):
        """На основе года рождения считаем текущий возраст"""
        return 2021 - self.date_birth


class Student(Human):
    """Создаем под класс студент на основе класса человек, добавляем такие параметры как возраст и факультет"""
    def __init__(self, name, surname, date_birth, mobile_phone: int, faculty="math"):
        super().__init__(name, surname, date_birth)
        self.faculty = faculty
        self.mobile_phone = mobile_phone

    def __str__(self):
        res = super().__str__()
        return f'{res}'  '\n'f'faculty: {self.faculty}' '\n'f'mobile phone: {self.mobile_phone}'


class Group:
    """На базе класс студент создаем список студентов"""

    def __init__(self, *students):
        self.students = students
        self.new_student = None
        self.student_magazine = []
        for student in students:
            if not student.surname in self.student_magazine and len(self.student_magazine) < MAX_STUDENTS + 1:
                self.student_magazine.append(student.surname)
            else:
                raise Custom_Excep



    def __str__(self):

        return f'{self.student_magazine} '

    def append_student(self, student):
        """Функция добавляет студента в список"""
        """Если студент уже в списке или список состоит больше чем из 10 человек выводим о недопустимости действия"""
        if not student.surname in self.student_magazine and len(self.student_magazine) < MAX_STUDENTS + 1:
           self.student_magazine.append(student.surname)
        else:
            raise Custom_Excep

    def delete_student(self, new_student):
        """Функция удаляет студента из списка"""
        if new_student.surname in self.student_magazine:
            self.student_magazine.remove(new_student.surname)
        else:
            print("No such student found")

    def find_student(self, new_student):
        """"Поиск студента в списке, если такой студент есть выведет информацию о нем, или выведет на экран что такого
        студента нет"""
        if new_student.surname in self.student_magazine:
            return new_student
        else:
            return None


if __name__ == "__main__":
    oleh = Student("Oleh", "Olehov", 1998, 7657657)
    ivanov = Student("Ivan", "Ivanov", 2000, 7657657657)
    petrov = Student("Petr", "Petrov", 1999, 7657657657)
    alexandr = Student("Alexandr", "Alex", 1995, 32132133)
    group = Group(oleh, ivanov)
    group.append_student(petrov)

