# ============================================================
# ИСКЛЮЧЕНИЯ И ОБРАБОТКА ОШИБОК В PYTHON
# ============================================================


# ============================================================
# БАЗОВАЯ КОНСТРУКЦИЯ: try / except
# ============================================================
# Код в блоке try выполняется, пока не возникнет исключение.
# Если исключение совпадает с указанным в except — оно перехватывается.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Нельзя делить на ноль")

# Получить объект исключения — через as
try:
    number = int("abc")
except ValueError as e:
    print(f"Ошибка: {e}")          # Ошибка: invalid literal for int() with base 10: 'abc'

# Перехватить несколько типов исключений
try:
    items = [1, 2, 3]
    print(items[10])
except (IndexError, KeyError) as e:
    print(f"Ошибка доступа: {e}")  # Ошибка доступа: list index out of range


# ============================================================
# else И finally
# ============================================================
# else   — выполняется если исключения НЕ было
# finally — выполняется ВСЕГДА (даже если было исключение)

def read_number(s):
    try:
        n = int(s)
    except ValueError:
        print("Не число")
    else:
        print(f"Успешно: {n}")     # выполнится только если int(s) не упал
    finally:
        print("Блок finally")      # выполнится в любом случае

read_number("42")
# Успешно: 42
# Блок finally

read_number("abc")
# Не число
# Блок finally

# finally типично используется для освобождения ресурсов:
# закрытие файла, соединения с БД и т.д.


# ============================================================
# ИЕРАРХИЯ ВСТРОЕННЫХ ИСКЛЮЧЕНИЙ
# ============================================================
# Все исключения наследуются от BaseException.
# Большинство пользовательских ошибок — от Exception.
#
# BaseException
# ├── SystemExit          — sys.exit()
# ├── KeyboardInterrupt   — Ctrl+C
# └── Exception
#     ├── ValueError      — неверное значение (int("abc"))
#     ├── TypeError       — неверный тип ("a" + 1)
#     ├── IndexError      — индекс за пределами списка
#     ├── KeyError        — ключ не найден в словаре
#     ├── AttributeError  — атрибут не существует
#     ├── NameError       — имя переменной не определено
#     ├── ZeroDivisionError
#     ├── FileNotFoundError
#     ├── OSError
#     └── ...

# Можно перехватить целую ветку иерархии
try:
    d = {}
    print(d["key"])
except LookupError as e:          # перехватит IndexError и KeyError
    print(f"LookupError: {e}")

# Exception перехватит почти всё — используй только если необходимо
try:
    int("x")
except Exception as e:
    print(f"{type(e).__name__}: {e}")


# ============================================================
# raise — выброс исключения
# ============================================================

def divide(a, b):
    if b == 0:
        raise ValueError("Делитель не может быть равен нулю")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(e)    # Делитель не может быть равен нулю

# raise без аргументов — перебрасывает текущее исключение дальше
def process(value):
    try:
        return int(value)
    except ValueError:
        print("Логируем ошибку...")
        raise               # пробрасываем исключение вызывающему коду

try:
    process("bad")
except ValueError:
    print("Поймали выше")


# ============================================================
# ЦЕПОЧКА ИСКЛЮЧЕНИЙ: raise ... from
# ============================================================
# Позволяет показать: "это исключение возникло из-за другого".

def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError(f"Не удалось загрузить конфиг: {path}") from e

try:
    load_config("config.json")
except RuntimeError as e:
    print(e)            # Не удалось загрузить конфиг: config.json
    print(e.__cause__)  # [Errno 2] No such file or directory: 'config.json'


# ============================================================
# ПОЛЬЗОВАТЕЛЬСКИЕ ИСКЛЮЧЕНИЯ
# ============================================================
# Наследуются от Exception (или его подклассов).
# Позволяют создавать осмысленную иерархию ошибок приложения.

class AppError(Exception):
    """Базовое исключение приложения."""


class ValidationError(AppError):
    """Ошибка валидации входных данных."""

    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"[{field}] {message}")


class NotFoundError(AppError):
    """Запрошенный ресурс не найден."""

    def __init__(self, resource, id):
        self.resource = resource
        self.id = id
        super().__init__(f"{resource} с id={id} не найден")


def create_user(name, age):
    if not name:
        raise ValidationError("name", "Имя не может быть пустым")
    if age < 0 or age > 150:
        raise ValidationError("age", "Возраст должен быть от 0 до 150")
    return {"name": name, "age": age}


def get_user(user_id, users):
    if user_id not in users:
        raise NotFoundError("User", user_id)
    return users[user_id]


# Обработка конкретных пользовательских исключений
try:
    create_user("", 25)
except ValidationError as e:
    print(f"Валидация: поле '{e.field}' — {e.message}")
    # Валидация: поле 'name' — Имя не может быть пустым

try:
    get_user(42, {})
except NotFoundError as e:
    print(e)    # User с id=42 не найден

# Ловим всю ветку AppError сразу
try:
    create_user("Alice", -5)
except AppError as e:
    print(f"Ошибка приложения: {e}")


# ============================================================
# КОНТЕКСТНЫЙ МЕНЕДЖЕР: with / as
# ============================================================
# with гарантирует освобождение ресурса даже при исключении —
# лучшая альтернатива try/finally для файлов, соединений и т.д.

# Запись в файл
with open("temp.txt", "w") as f:
    f.write("hello")
# файл закрыт автоматически после выхода из блока with

# Чтение файла
with open("temp.txt") as f:
    content = f.read()
    print(content)      # hello

# Эквивалент без with:
f = open("temp.txt")
try:
    content = f.read()
finally:
    f.close()           # нужно не забыть — with делает это автоматически


# ============================================================
# СВОЙ КОНТЕКСТНЫЙ МЕНЕДЖЕР
# ============================================================
# Нужно реализовать __enter__ и __exit__.
# __exit__ получает информацию об исключении — может его подавить.

class ManagedResource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Открываем {self.name}")
        return self             # возвращается как as-переменная

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Закрываем {self.name}")
        # Вернуть True — подавить исключение, False/None — пробросить дальше
        return False


with ManagedResource("соединение") as res:
    print(f"Работаем с {res.name}")
# Открываем соединение
# Работаем с соединение
# Закрываем соединение


# ============================================================
# contextlib.contextmanager — контекстный менеджер через генератор
# ============================================================
# Более лаконичный способ без класса.

from contextlib import contextmanager


@contextmanager
def timer(label):
    import time
    start = time.time()
    try:
        yield                           # здесь выполняется тело with-блока
    finally:
        elapsed = time.time() - start
        print(f"{label}: {elapsed:.4f}с")


with timer("вычисление"):
    total = sum(range(1_000_000))
# вычисление: 0.0312с  (время будет разным)


# ============================================================
# ПОДАВЛЕНИЕ ИСКЛЮЧЕНИЙ: contextlib.suppress
# ============================================================
# Аккуратная замена пустого except-блока.

import os
from contextlib import suppress

# Вместо:
try:
    os.remove("temp.txt")
except FileNotFoundError:
    pass

# Можно написать:
with suppress(FileNotFoundError):
    os.remove("temp.txt")
