"""Неделя 1: функции, классы, генераторы, comprehension.

Запуск: python 01_functions_generators.py
"""


def mean(values):
    """Среднее арифметическое списка чисел."""
    return sum(values) / len(values)


def fibonacci(n):
    """Генератор: первые n чисел Фибоначчи."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


class Vector:
    """Двумерный вектор со сложением и умножением на число."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


if __name__ == "__main__":
    # list comprehension: квадраты чётных чисел
    squares = [n * n for n in range(10) if n % 2 == 0]
    print(squares)                      # [0, 4, 16, 36, 64]

    # dict comprehension: длины слов
    lengths = {word: len(word) for word in ["ml", "python", "numpy"]}
    print(lengths)                      # {'ml': 2, 'python': 6, 'numpy': 5}

    print(mean([4, 8, 15, 16, 23, 42]))  # 18.0
    print(list(fibonacci(10)))          # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print(Vector(1, 2) + Vector(3, -1))  # Vector(4, 1)
    print(Vector(3, 1) * 2)             # Vector(6, 2)
