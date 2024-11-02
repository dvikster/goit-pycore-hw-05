def caching_fibonacci():
    # Створюю порожній словник для кешування
    cache = {}

    # Внутрішня функція fibonacci, що обчислює числа Фібоначчі
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Перевіряю, чи значення вже є в кеші
        if n in cache:
            return cache[n]
        
        # Обчислюєю та зберігаю результат у кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаю внутрішню функцію fibonacci
    return fibonacci

# Отримую функцію fibonacci
fib = caching_fibonacci()

# Використовую функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
