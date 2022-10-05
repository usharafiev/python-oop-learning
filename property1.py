from string import digits


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def is_include_all_register(password):
        for i in range(len(password)):
            if password[i].islower() is True:
                if password[i].isupper() is True:
                    return True
            else:
                break
        return False

    @staticmethod
    def is_include_only_latin(password):
        if password.isalnum() is True:
            return True

    @staticmethod
    def check_password_dictionary(password):
        passwordlist = open('easy_passwords.txt')
        for line in passwordlist:
            if line == password:
                return True
        return False

    @login.setter
    def login(self, value):
        if value.count('@') != 1:
            raise ValueError("Логин должен содержать один символ '@'")
        if value.find('@') > value.find('.'):
            raise ValueError("Логин должен содержать символ '.'")
        else:
            self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if 5 > len(value) > 11:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_number(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = value


r1 = Registration('qwerty@rambler.ru', 'QwrRt124')  # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

# теперь пытаемся запись плохие пароли
r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
# r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
# r1.password = 43  # raise TypeError("Пароль должен быть строкой")
