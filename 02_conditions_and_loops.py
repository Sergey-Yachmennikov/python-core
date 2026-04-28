# ============================================================
# УСЛОВИЯ В PYTHON
# ============================================================

age = 20

# --- if / elif / else ---
if age < 18:
    print("Несовершеннолетний")
elif age < 65:
    print("Взрослый")
else:
    print("Пенсионер")

# --- Тернарный оператор (одна строка) ---
status = "совершеннолетний" if age >= 18 else "несовершеннолетний"
print(status)

# --- Логические операторы: and, or, not ---
is_member = True
has_discount = False

if is_member and not has_discount:
    print("Участник без скидки")

if age > 18 or is_member:
    print("Доступ разрешён")

# --- Сравнение: ==, !=, >, <, >=, <= ---
print(10 == 10)     # True
print(10 != 5)      # True
print(5 > 3)        # True

# --- Проверка на None ---
value = None
if value is None:
    print("Значение не задано")

# --- Проверка вхождения: in ---
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Банан есть в списке")


# ============================================================
# MATCH / CASE (аналог switch — появился в Python 3.10)
# ============================================================

command = "quit"

match command:
    case "start":
        print("Запуск...")
    case "stop":
        print("Остановка...")
    case "quit":
        print("Выход...")
    case _:                         # _ — default (любое другое значение)
        print("Неизвестная команда")

# match умеет сравнивать несколько значений в одном case
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Выходной")
    case _:
        print("Рабочий день")

# match с условием (guard)
score = 85

match score:
    case n if n >= 90:
        print("Отлично")
    case n if n >= 70:
        print("Хорошо")
    case _:
        print("Нужно подтянуться")


# ============================================================
# ЦИКЛ for
# ============================================================

# --- Перебор списка ---
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# --- range() — диапазон чисел ---
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (шаг 2)
    print(i)

for i in range(5, 0, -1):   # 5, 4, 3, 2, 1 (обратный порядок)
    print(i)

# --- enumerate() — индекс + значение ---
for index, color in enumerate(colors):
    print(f"{index}: {color}")

# --- Перебор строки (строка — это последовательность символов) ---
for char in "hello":
    print(char)

# --- Перебор словаря ---
person = {"name": "Alice", "age": 25, "city": "Moscow"}

for key in person:                      # только ключи
    print(key)

for value in person.values():           # только значения
    print(value)

for key, value in person.items():       # ключ и значение
    print(f"{key} = {value}")

# --- zip() — параллельный перебор двух списков ---
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 92]

for name, score in zip(names, scores):
    print(f"{name}: {score}")


# ============================================================
# ЦИКЛ while
# ============================================================

# --- Базовый while ---
count = 0
while count < 5:
    print(count)
    count += 1

# --- while True — бесконечный цикл (выход через break) ---
number = 0
while True:
    number += 1
    if number == 3:
        break           # немедленный выход из цикла
    print(number)

# --- while с else ---
# else выполняется если цикл завершился без break
n = 0
while n < 3:
    print(n)
    n += 1
else:
    print("Цикл завершён нормально")


# ============================================================
# УПРАВЛЕНИЕ ЦИКЛОМ: break, continue, pass
# ============================================================

# break — выход из цикла
for i in range(10):
    if i == 5:
        break
    print(i)           # выведет 0, 1, 2, 3, 4

# continue — пропустить текущую итерацию
for i in range(5):
    if i == 2:
        continue
    print(i)           # выведет 0, 1, 3, 4

# pass — ничего не делать (заглушка)
for i in range(3):
    pass               # цикл выполнится, но без действий

# --- for с else ---
# else выполняется если цикл не был прерван через break
for i in range(5):
    if i == 10:        # условие никогда не выполнится
        break
else:
    print("break не случился")


# ============================================================
# LIST COMPREHENSION — компактный способ создать список
# ============================================================

# Обычный цикл:
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

# То же самое в одну строку:
squares = [i ** 2 for i in range(1, 6)]
print(squares)          # [1, 4, 9, 16, 25]

# С условием:
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(even_squares)     # [4, 16, 36, 64, 100]
