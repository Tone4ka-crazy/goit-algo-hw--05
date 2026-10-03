import re
from typing import Callable

def generator_numbers(text:str):
    #аналізує текст, шукає дійсні числа та повертає їх як генератор
    numbers = re.findall(r"\b\d+\.\d+\b", text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    #обчислює загальну суму чисел у тексті за допомогою переданого генератора
    return sum(func(text))
