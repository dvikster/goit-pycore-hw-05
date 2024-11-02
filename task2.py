import re
from typing import Callable

# Функція generator_numbers, яка повертає генератор для дійсних чисел у тексті
def generator_numbers(text: str):
    # Використовую регулярний вираз для пошуку дійсних чисел, відокремлених пробілами
    numbers = re.findall(r'\b\d+\.\d+\b', text)
    # Конвертую знайдені числа в float і генерую їх одне за одним
    for number in numbers:
        yield float(number)

# Функція sum_profit для підсумовування всіх чисел із generator_numbers
def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
