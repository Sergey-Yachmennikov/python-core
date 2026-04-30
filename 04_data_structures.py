# ============================================================
# СТРУКТУРЫ ДАННЫХ В PYTHON
# ============================================================
#
# Встроенные:
#   list    — упорядоченный изменяемый список
#   tuple   — упорядоченный неизменяемый список
#   dict    — словарь (ключ: значение)
#   set     — множество уникальных элементов
#   frozenset — неизменяемое множество
#
# Из модуля collections:
#   deque        — двусторонняя очередь
#   namedtuple   — кортеж с именованными полями
#   defaultdict  — словарь с дефолтным значением
#   Counter      — счётчик элементов
#   OrderedDict  — словарь с сохранением порядка вставки
# ============================================================


# ============================================================
# LIST — список
# ============================================================
# Упорядоченный, изменяемый, допускает дубликаты.

fruits = ["apple", "banana", "cherry"]

# Доступ по индексу (с конца — отрицательный индекс)
print(fruits[0])        # apple
print(fruits[-1])       # cherry

# Срез [start:stop:step]
print(fruits[0:2])      # ['apple', 'banana']
print(fruits[::-1])     # ['cherry', 'banana', 'apple'] — разворот

# Изменение
fruits[1] = "mango"

# Добавление
fruits.append("orange")        # добавить в конец
fruits.insert(1, "kiwi")       # вставить по индексу
fruits.extend(["grape", "pear"]) # добавить несколько

# Удаление
fruits.remove("kiwi")          # удалить по значению (первое вхождение)
popped = fruits.pop()          # удалить и вернуть последний элемент
popped = fruits.pop(0)         # удалить и вернуть по индексу
del fruits[0]                  # удалить по индексу

# Поиск и проверка
print("apple" in fruits)       # True / False
print(fruits.index("mango"))   # индекс элемента
print(fruits.count("apple"))   # количество вхождений

# Сортировка
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()                  # сортировка на месте (изменяет список)
numbers.sort(reverse=True)      # по убыванию
sorted_copy = sorted(numbers)   # возвращает новый список, оригинал не меняет

# Длина, минимум, максимум, сумма
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Очистка
numbers.clear()


# ============================================================
# TUPLE — кортеж
# ============================================================
# Упорядоченный, НЕИЗМЕНЯЕМЫЙ. Быстрее списка, занимает меньше памяти.
# Используется для данных, которые не должны меняться.

point = (10, 20)
rgb = (255, 128, 0)
single = (42,)          # кортеж из одного элемента — обязательна запятая

# Доступ — как у списка
print(point[0])         # 10
print(point[-1])        # 20

# Распаковка
x, y = point
print(x, y)             # 10 20

r, g, b = rgb

# Расширенная распаковка
first, *rest = (1, 2, 3, 4, 5)
print(first)    # 1
print(rest)     # [2, 3, 4, 5]

# Кортеж можно использовать как ключ словаря (список — нельзя, он изменяемый)
locations = {(55.75, 37.61): "Москва", (59.93, 30.32): "Санкт-Петербург"}

# Методы (только два — изменять нельзя)
t = (1, 2, 2, 3)
print(t.count(2))       # 2
print(t.index(3))       # 3


# ============================================================
# DICT — словарь
# ============================================================
# Неупорядоченный (с Python 3.7 сохраняет порядок вставки),
# изменяемый, ключи уникальны.

person = {
    "name": "Alice",
    "age": 25,
    "city": "Moscow"
}

# Доступ
print(person["name"])               # Alice
print(person.get("age"))            # 25
print(person.get("email", "n/a"))   # n/a — дефолт если ключа нет
# person["email"] — KeyError если ключа нет

# Добавление и изменение
person["email"] = "alice@mail.ru"
person["age"] = 26

# Удаление
del person["city"]
removed = person.pop("email")       # удалить и вернуть значение
person.popitem()                    # удалить последнюю добавленную пару

# Проверка
print("name" in person)             # True — проверяет ключи

# Перебор
for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")

# Слияние словарей
defaults = {"color": "red", "size": 10}
custom   = {"color": "blue", "weight": 5}

merged = {**defaults, **custom}     # custom перезапишет совпадающие ключи
# {'color': 'blue', 'size': 10, 'weight': 5}

# Python 3.9+: оператор |
merged = defaults | custom

# setdefault — установить значение только если ключа нет
person.setdefault("role", "user")

# update — обновить несколько ключей сразу
person.update({"age": 27, "city": "SPb"})

# Создание словаря из двух списков
keys   = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))         # {'a': 1, 'b': 2, 'c': 3}

# Dict comprehension
squares = {x: x ** 2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ============================================================
# SET — множество
# ============================================================
# Неупорядоченное, изменяемое, только уникальные элементы.
# Быстрая проверка вхождения (O(1)).

colors = {"red", "green", "blue"}
empty_set = set()               # ВАЖНО: {} создаёт dict, не set!

# Добавление и удаление
colors.add("yellow")
colors.discard("red")           # удалить, не ругаться если нет
colors.remove("green")          # удалить, KeyError если нет

# Проверка
print("blue" in colors)         # True

# Удаление дублей из списка
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))        # [1, 2, 3, 4] — порядок не гарантирован

# Операции над множествами
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)        # объединение:      {1, 2, 3, 4, 5, 6}
print(a & b)        # пересечение:      {3, 4}
print(a - b)        # разность:         {1, 2}
print(a ^ b)        # симметр. разность: {1, 2, 5, 6} (есть в одном, но не в обоих)

print(a.issubset({1, 2, 3, 4, 5}))     # True — a входит в другое множество
print(a.issuperset({1, 2}))            # True — a содержит другое множество
print(a.isdisjoint({7, 8}))            # True — нет общих элементов


# ============================================================
# FROZENSET — неизменяемое множество
# ============================================================
# Как set, но нельзя изменить после создания.
# Можно использовать как ключ словаря.

fs = frozenset([1, 2, 3, 2, 1])
print(fs)           # frozenset({1, 2, 3})

allowed_roles = frozenset({"admin", "editor", "viewer"})
if "admin" in allowed_roles:
    print("Доступ разрешён")


# ============================================================
# collections.deque — двусторонняя очередь
# ============================================================
# Быстрое добавление/удаление с обоих концов (O(1)).
# Список медленнее при операциях с началом (O(n)).

from collections import deque

queue = deque([1, 2, 3])

queue.append(4)         # добавить справа
queue.appendleft(0)     # добавить слева
queue.pop()             # удалить справа
queue.popleft()         # удалить слева

print(queue)            # deque([1, 2, 3])

# maxlen — автоматически удаляет старые элементы
log = deque(maxlen=3)
for i in range(6):
    log.append(i)
print(log)              # deque([3, 4, 5], maxlen=3)


# ============================================================
# collections.namedtuple — кортеж с именованными полями
# ============================================================

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)

print(p.x)          # 10 — доступ по имени
print(p[0])         # 10 — доступ по индексу (как обычный кортеж)
print(p)            # Point(x=10, y=20)

# Неизменяемый — как tuple
# p.x = 5   # AttributeError


# ============================================================
# collections.defaultdict — словарь с дефолтным значением
# ============================================================
# Не бросает KeyError для отсутствующих ключей.

from collections import defaultdict

# Группировка слов по первой букве
words = ["apple", "ant", "banana", "avocado", "blueberry"]

grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)

print(dict(grouped))
# {'a': ['apple', 'ant', 'avocado'], 'b': ['banana', 'blueberry']}

# Подсчёт без проверки существования ключа
counter = defaultdict(int)
for word in words:
    counter[word[0]] += 1

print(dict(counter))    # {'a': 3, 'b': 2}


# ============================================================
# collections.Counter — счётчик элементов
# ============================================================

from collections import Counter

text = "abracadabra"
c = Counter(text)
print(c)                        # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

print(c.most_common(2))         # [('a', 5), ('b', 2)] — топ 2

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
wc = Counter(words)
print(wc["apple"])              # 3

# Арифметика счётчиков
c1 = Counter(a=3, b=2)
c2 = Counter(a=1, b=4)
print(c1 + c2)                  # Counter({'b': 6, 'a': 4})
print(c1 - c2)                  # Counter({'a': 2})
