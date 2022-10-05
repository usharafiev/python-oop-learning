from string import digits


class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        print('getter called')
        return self.__password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) < 4:
            raise ValueError('Длина пароля слишком мала, минимум 4 символа')
        if len(value) > 12:
            raise ValueError('Длина пароля слишком велика, максимум 12 символа')
        if not User.is_include_number(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        self.__password = value

Проверка на включение в словарь паролей сделать
