class strtoupstr:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())


processor = strtoupstr()
processor.getString()
processor.printString()


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2



class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Точка ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5




class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  
            print(f"Внесено: {amount}. Баланс: {self.balance}")
        else:
            print("Сумма внесения должна быть положительной")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Снято: {amount}. Баланс: {self.balance}")
        else:
            print("Недостаточно средств на балансе")

    def __str__(self):
        return f"Владелец: {self.owner}\n Баланс: {self.balance}"



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


