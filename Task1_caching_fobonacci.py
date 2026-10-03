def caching_fibonacci():
    #Порожній словник для зберігання результатів завдяки замиканню
    cache = {}
    def fibonacci(n):
        # Базові випадки рекурсії
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Якщо число вже обчислювалось раніше, повертаємо його з кешу
        if n in cache:
            return cache[n]
        # Якщо числа немає в кеші, обчислюємо його рекурсивно і записуємо у словник
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо внутрішню функцію як об'єкт
    return fibonacci
