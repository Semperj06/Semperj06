

class Human:
    """Описываем человека его имя, фамилия, год рождения и отчество если есть"""
    def __init__(self, name: str, surname: str, date_birth: int):
        self.name = name.title()
        self.surname = surname.title()
        self.date_birth = date_birth

    def __str__(self):
        return f'{self.name} {self.surname[0]}.' '\n'f'Age: {self.age()} date of birth: {self.date_birth}'

    def age(self):
        """На основе года рождения считаем текущий возраст"""
        return 2021 - self.date_birth