import exeption
import main
import sequence


class Group:
    """На базе класс студент создаем список студентов"""

    def __init__(self, *students):
        self.students = students
        self.new_student = None
        self.student_magazine = []
        for student in students:
            self.append_student(student)

    def __str__(self):
        res = ", ".join(self.student_magazine)
        return f'{res}'

    def append_student(self, student):
        """Функция добавляет студента в список"""
        """Если студент уже в списке или список состоит больше чем из 10 человек выводим о недопустимости действия"""
        if not student.surname in self.student_magazine and len(self.student_magazine) < main.MAX_STUDENTS + 1:
           self.student_magazine.append(student.surname)
        else:
            raise exeption.Custom_Excep

    def delete_student(self, new_student):
        """Функция удаляет студента из списка"""
        if new_student.surname in self.student_magazine:
            self.student_magazine.remove(new_student.surname)

    def find_student(self, new_student):
        """"Поиск студента в списке, если такой студент есть выведет информацию о нем, или выведет на экран что такого
        студента нет"""
        if new_student.surname in self.student_magazine:
            return new_student
        else:
            return None

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < len(self.student_magazine):
                return self.student_magazine[index]
            else:
                raise IndexError

        if isinstance(index, slice):
            result = []
            start = index.start or 0
            stop = index.stop or -1
            step = index.step or 1
            if start >= 0 and stop <= len(self.student_magazine):
                for elem in range(start, stop, step):
                    result.append(self.student_magazine[elem])
                return result
            else:
                raise IndexError
        else:
            raise TypeError()

    def __len__(self):
        return len(self.shopping_basket)