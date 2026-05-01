# ============================================================
# ООП В PYTHON: КЛАССЫ, НАСЛЕДОВАНИЕ, ПОЛИМОРФИЗМ
# ============================================================

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


# ============================================================
# КЛАСС И ОБЪЕКТ
# ============================================================
# class — шаблон (тип). Объект — конкретный экземпляр класса.
# __init__ — конструктор, вызывается при создании объекта.
# self — ссылка на текущий экземпляр (аналог this в других языках).

class Dog:
    # Атрибут класса — общий для всех экземпляров
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Атрибуты экземпляра — у каждого объекта свои
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} говорит: Гав!")

    def description(self):
        return f"{self.name}, {self.age} лет"


rex = Dog("Rex", 3)
buddy = Dog("Buddy", 5)

rex.bark()                      # Rex говорит: Гав!
print(rex.description())        # Rex, 3 лет
print(buddy.name)               # Buddy
print(Dog.species)              # Canis familiaris — доступ через класс
print(rex.species)              # Canis familiaris — доступ через экземпляр


# ============================================================
# DUNDER-МЕТОДЫ (магические методы)
# ============================================================
# Имена вида __method__ — специальные методы Python.
# Позволяют задать поведение встроенных операций для своих классов.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Строка для разработчика: eval(repr(obj)) == obj (в идеале)
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        # Строка для пользователя: используется в print()
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        # Оператор +
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        # Оператор * (умножение на число)
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        # Оператор ==
        return self.x == other.x and self.y == other.y

    def __len__(self):
        # len() — возвращает "длину" объекта
        return int(math.sqrt(self.x ** 2 + self.y ** 2))


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1)           # (1, 2)          — вызывает __str__
print(repr(v1))     # Vector(1, 2)    — вызывает __repr__
print(v1 + v2)      # (4, 6)          — вызывает __add__
print(v1 * 3)       # (3, 6)          — вызывает __mul__
print(v1 == v2)     # False           — вызывает __eq__
print(len(v2))      # 5               — вызывает __len__


# ============================================================
# ИНКАПСУЛЯЦИЯ: публичные, защищённые и приватные атрибуты
# ============================================================
# Python не запрещает доступ жёстко, но есть соглашения:
#   name     — публичный
#   _name    — защищённый (не трогать снаружи — договорённость)
#   __name   — приватный (name mangling — _ClassName__name)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # публичный
        self._balance = balance     # защищённый (внутренний)
        self.__pin = 1234           # приватный (скрытый снаружи)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return self._balance

    def __repr__(self):
        return f"BankAccount({self.owner!r}, balance={self._balance})"


account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())    # 1300
print(account)                  # BankAccount('Alice', balance=1300)

# account.__pin               # AttributeError
# account._BankAccount__pin   # 1234 — технически доступно, но не надо


# ============================================================
# СВОЙСТВА: @property
# ============================================================
# Позволяют обращаться к методам как к атрибутам.
# Удобно для валидации и вычисляемых значений.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Радиус не может быть отрицательным")
        self._radius = value

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2


c = Circle(5)
print(c.radius)     # 5      — геттер
print(c.area)       # 78.53…
print(c.diameter)   # 10

c.radius = 10       # сеттер
print(c.area)       # 314.15…

# c.radius = -1     # ValueError


# ============================================================
# НАСЛЕДОВАНИЕ
# ============================================================
# Дочерний класс наследует атрибуты и методы родительского.
# super() — вызов метода родителя.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Подкласс должен реализовать speak()")

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"


class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит: Мяу!"


class Duck(Animal):
    def speak(self):
        return f"{self.name} говорит: Кря!"


class PoliceDog(Dog):
    def __init__(self, name, age, badge_number):
        super().__init__(name, age)     # вызов конструктора родителя
        self.badge_number = badge_number

    def description(self):
        base = super().description()    # вызов метода родителя
        return f"{base}, жетон #{self.badge_number}"


cat = Cat("Мурка")
duck = Duck("Кряква")
police_dog = PoliceDog("Рекс", 4, 42)

print(cat.speak())              # Мурка говорит: Мяу!
print(duck.speak())             # Кряква говорит: Кря!
print(police_dog.description()) # Рекс, 4 лет, жетон #42

# Проверка принадлежности к классу
print(isinstance(cat, Cat))     # True
print(isinstance(cat, Animal))  # True — Cat является Animal
print(issubclass(Cat, Animal))  # True


# ============================================================
# ПОЛИМОРФИЗМ
# ============================================================
# Один интерфейс — разное поведение в зависимости от класса.
# Python использует "утиную типизацию": если объект умеет speak() —
# можно вызвать speak(), не проверяя тип.

animals = [Cat("Барсик"), Duck("Утёнок"), PoliceDog("Граф", 2, 7)]

for animal in animals:
    # У каждого объекта свой speak(), но вызываем одинаково
    print(animal.speak())

# Cat, Duck — реализовали speak()
# PoliceDog — унаследовал bark() от Dog, но не Animal.speak()
# Поэтому для полного полиморфизма классы должны следовать одному контракту.


# ============================================================
# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ И MRO
# ============================================================
# Python позволяет наследоваться от нескольких классов.
# Порядок поиска метода — MRO (Method Resolution Order), алгоритм C3.

class Flyable:
    def move(self):
        return "Лечу"


class Swimmable:
    def move(self):
        return "Плыву"


class FlyingFish(Flyable, Swimmable):
    pass


class Amphibian(Swimmable, Flyable):
    pass


ff = FlyingFish()
am = Amphibian()

print(ff.move())        # Лечу    — Flyable идёт первым в MRO
print(am.move())        # Плыву   — Swimmable идёт первым в MRO

# Посмотреть порядок разрешения методов:
print(FlyingFish.__mro__)
# (<class 'FlyingFish'>, <class 'Flyable'>, <class 'Swimmable'>, <class 'object'>)


# ============================================================
# АБСТРАКТНЫЕ КЛАССЫ
# ============================================================
# ABC (Abstract Base Class) — класс, от которого нельзя создать объект.
# Служит контрактом: подкласс ОБЯЗАН реализовать абстрактные методы.

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"Площадь: {self.area():.2f}, периметр: {self.perimeter():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# shape = Shape()       # TypeError: нельзя создать экземпляр ABC

rect = Rectangle(4, 6)
circ = CircleShape(5)

print(rect.describe())  # Площадь: 24.00, периметр: 20.00
print(circ.describe())  # Площадь: 78.54, периметр: 31.42

shapes = [rect, circ]
for s in shapes:
    print(f"area = {s.area():.2f}")


# ============================================================
# СТАТИЧЕСКИЕ МЕТОДЫ И МЕТОДЫ КЛАССА
# ============================================================

class Temperature:
    unit = "Celsius"

    def __init__(self, degrees):
        self.degrees = degrees

    @classmethod
    def from_fahrenheit(cls, f):
        # Альтернативный конструктор. cls — это сам класс, не экземпляр.
        return cls((f - 32) * 5 / 9)

    @classmethod
    def set_unit(cls, unit):
        cls.unit = unit

    @staticmethod
    def is_freezing(celsius):
        # Не использует ни self, ни cls — просто утилита, связанная с классом.
        return celsius <= 0

    def __repr__(self):
        return f"{self.degrees:.1f}° {Temperature.unit}"


t1 = Temperature(100)
t2 = Temperature.from_fahrenheit(212)   # альтернативный конструктор

print(t1)                               # 100.0° Celsius
print(t2)                               # 100.0° Celsius
print(Temperature.is_freezing(-5))      # True
print(Temperature.is_freezing(20))      # False

Temperature.set_unit("°C")
print(t1)                               # 100.0° °C


# ============================================================
# DATACLASS — удобный способ создать класс-контейнер
# ============================================================
# @dataclass автоматически генерирует __init__, __repr__, __eq__

@dataclass
class Point3D:
    x: float
    y: float
    z: float = 0.0      # значение по умолчанию


@dataclass
class Player:
    name: str
    health: int = 100
    inventory: list = field(default_factory=list)   # изменяемый дефолт

    def pick_up(self, item):
        self.inventory.append(item)


p = Point3D(1.0, 2.0)
print(p)            # Point3D(x=1.0, y=2.0, z=0.0)
print(p == Point3D(1.0, 2.0, 0.0))     # True — __eq__ сгенерирован

player = Player("Alice")
player.pick_up("меч")
player.pick_up("щит")
print(player)       # Player(name='Alice', health=100, inventory=['меч', 'щит'])
