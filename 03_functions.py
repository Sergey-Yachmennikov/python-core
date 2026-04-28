# ============================================================
# ФУНКЦИИ В PYTHON
# ============================================================

# Функция объявляется через def.
# Вызов функции — имя + круглые скобки.

def greet():
    print("Привет!")

greet()


# ============================================================
# ПАРАМЕТРЫ И АРГУМЕНТЫ
# ============================================================

# --- Обычные параметры ---
def greet_user(name):
    print(f"Привет, {name}!")

greet_user("Alice")

# --- Несколько параметров ---
def add(a, b):
    return a + b

result = add(3, 5)
print(result)           # 8

# --- Значения по умолчанию ---
# Параметры со значением по умолчанию идут ПОСЛЕ обычных
def greet_with_role(name, role="гость"):
    print(f"Привет, {name}! Роль: {role}")

greet_with_role("Alice")            # роль = "гость"
greet_with_role("Bob", "админ")     # роль = "админ"

# --- Именованные аргументы (keyword arguments) ---
# Можно передавать в любом порядке, указывая имя параметра
def describe(name, age, city):
    print(f"{name}, {age} лет, из {city}")

describe(age=25, city="Moscow", name="Alice")


# ============================================================
# *args — произвольное количество аргументов
# ============================================================

# *args собирает все позиционные аргументы в кортеж
def total(*args):
    print(args)             # (1, 2, 3, 4) — это кортеж
    return sum(args)

print(total(1, 2, 3, 4))   # 10
print(total(5, 10))         # 15


# ============================================================
# **kwargs — произвольное количество именованных аргументов
# ============================================================

# **kwargs собирает все именованные аргументы в словарь
def show_info(**kwargs):
    print(kwargs)           # {"name": "Alice", "age": 25}
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=25, city="Moscow")

# --- Комбинация: обычные + *args + **kwargs ---
# Порядок всегда: обычные, *args, **kwargs
def mixed(required, *args, **kwargs):
    print(f"Обязательный: {required}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

mixed("важное", 1, 2, 3, name="Alice", age=25)


# ============================================================
# ВОЗВРАТ ЗНАЧЕНИЙ
# ============================================================

# --- return возвращает одно значение ---
def square(n):
    return n ** 2

# --- return нескольких значений (на самом деле возвращает кортеж) ---
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(low, high)            # 1 9

# --- Ранний выход из функции ---
def divide(a, b):
    if b == 0:
        return None         # ранний выход
    return a / b

# --- Функция без return возвращает None ---
def do_nothing():
    pass

print(do_nothing())         # None


# ============================================================
# ОБЛАСТЬ ВИДИМОСТИ (SCOPE)
# ============================================================

# Переменные внутри функции — локальные, снаружи не видны
def local_example():
    local_var = "я локальная"
    print(local_var)

local_example()
# print(local_var)  # ошибка — переменная не существует снаружи

# Глобальная переменная видна внутри функции (только для чтения)
global_var = "я глобальная"

def read_global():
    print(global_var)       # работает

read_global()

# Чтобы изменить глобальную переменную — нужен global
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)              # 2


# ============================================================
# LAMBDA — анонимная функция
# ============================================================

# lambda аргументы: выражение
# Только одно выражение, результат возвращается автоматически

square = lambda x: x ** 2
print(square(5))            # 25

add = lambda a, b: a + b
print(add(3, 4))            # 7

# Чаще всего lambda используют там, где нужна короткая функция
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort(key=lambda x: -x)     # сортировка по убыванию
print(numbers)              # [9, 5, 4, 3, 2, 1, 1]

words = ["banana", "apple", "kiwi", "cherry"]
words.sort(key=lambda w: len(w))    # сортировка по длине слова
print(words)                # ['kiwi', 'apple', 'banana', 'cherry']


# ============================================================
# ФУНКЦИИ КАК ОБЪЕКТЫ ПЕРВОГО КЛАССА
# ============================================================

# Функцию можно передать в другую функцию как аргумент
def apply(func, value):
    return func(value)

print(apply(square, 4))     # 16
print(apply(str, 100))      # "100"

# Функцию можно вернуть из другой функции
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))            # 10
print(triple(5))            # 15


# ============================================================
# ВСТРОЕННЫЕ ФУНКЦИИ ВЫСШЕГО ПОРЯДКА
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

# map() — применить функцию к каждому элементу
squared = list(map(lambda x: x ** 2, numbers))
print(squared)              # [1, 4, 9, 16, 25, 36]

# filter() — отфильтровать элементы по условию
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)                # [2, 4, 6]

# --- List comprehension часто читается лучше, чем map/filter ---
squared = [x ** 2 for x in numbers]
evens   = [x for x in numbers if x % 2 == 0]


# ============================================================
# РЕКУРСИЯ
# ============================================================

# Функция вызывает саму себя.
# Обязательно должно быть базовое условие (выход из рекурсии).

def factorial(n):
    if n == 0:              # базовый случай
        return 1
    return n * factorial(n - 1)

print(factorial(5))         # 120  (5 * 4 * 3 * 2 * 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))        # 55
