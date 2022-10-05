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
                check_a = True
        for j in range(len(password)):
            if password[j].isupper() is True and check_a == True:
                return True
        return False

    @staticmethod
    def is_include_only_latin(password):
        if password.isascii() is True:
            return True

    @staticmethod
    def check_password_dictionary(password):
        easy_passwords = []
        with open('easy_passwords.txt') as inf:
            for line in inf:
                line = line.strip()
                easy_passwords.append(line)
            if password in easy_passwords:
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
        elif not Registration.is_include_number(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        elif not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        elif not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        elif Registration.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        else:
            self.__password = value


r1 = Registration('qwerty@rambler.ru', 'QwrRt124')  # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124
r1.password = 'QwerTy123'
# теперь пытаемся запись плохие пароли
#r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
#r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
#r1.password = 43  # raise TypeError("Пароль должен быть строкой")
