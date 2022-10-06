class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.__balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.__balance += value

    def payment(self, value):
        if value <= self.__balance:
            self.__balance -= value
            return True
        else:
            print('Не хватает средств на балансе. Пополните счет')
            return False


import collections


class Cart:

    def __init__(self, user):
        self.user = user
        self.goods = collections.defaultdict(dict)
        self.__total = 0

    def add(self, product, amount=1):
        if not isinstance(self.goods[product.name], int):
            self.goods[product.name] = 0
        self.goods[product.name] = int(self.goods[product.name]) + amount
        self.__total += product.price * amount

    def remove(self, product, amount=1):
        if not isinstance(self.goods[product.name], int):
            self.goods[product.name] = 0
        if int(self.goods[product.name]) >= amount and product.price * amount <= self.__total:
            self.goods[product] = int(self.goods[product.name]) - amount
            self.__total -= product.price * amount
        else:
            self.__total = 0
            for element in self.goods:



    @property
    def total(self):
        return self.__total

    def order(self):
        if self.__total < self.user.balance:
            self.user.payment(self.__total)
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        res = sorted(self.goods.items(), key=lambda x: (-x[1], x[0]))
        for element in res:
            print(element)

        print(f'---Total: {self.__total}---')


billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user)  # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total)  # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order()  # Заказ оплачен
print(cart_billy.user.balance)  # 20
