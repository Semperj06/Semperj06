import group
import students
import sys
MAX_STUDENTS = 10

if __name__ == "__main__":
    oleh = students.Student("oleh", "alehov", 1998, 7657657)
    ivanov = students.Student("Ivan", "Ivanov", 2000, 7657657657)
    petrov = students.Student("Petr", "Petrov", 1999, 7657657657)
    alexandr = students.Student("Alexandr", "Alex", 1995, 32132133)
    dima = students.Student("dmitriy", "dmitro", 1998, 998765)
    group = group.Group(oleh, ivanov, petrov, alexandr)
    group.append_student(dima)
