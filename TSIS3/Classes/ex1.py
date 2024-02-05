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

# Пример использования
square = Square(4)
print(square.area())


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Пример использования
rectangle = Rectangle(4, 5)
print(rectangle.area())


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

# Пример использования
p1 = Point(0, 0)
p2 = Point(3, 4)
p1.show()
print("Расстояние:", p1.dist(p2))


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Баланс пополнен на {amount}. Текущий баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
        else:
            self.balance -= amount
            print(f"Снято {amount}. Текущий баланс: {self.balance}")

# Пример использования
account = Account("Иван", 100)
account.deposit(50)
account.withdraw(20)
account.withdraw(200)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 23, 29]
primes = list(filter(lambda x: is_prime(x), numbers))
print(primes)
