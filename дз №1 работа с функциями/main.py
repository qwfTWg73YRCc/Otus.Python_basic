
import operator
import math
import time
import functools
import random


TYPE_EVEN = 1
TYPE_ODD = 2
TYPE_PRIME = 3
'''
Функция №1.
Принимает список из N целых чисел 
и выдаёт список из них возведённых в заданную степень
'''


def my_pow_map(numbers=[1], expo=2):
    expon = []
    for i in numbers:
        expon.append(expo)
    return list(map(operator.pow, numbers, expon))


'''
Функция №2: принимает на вход список из целых чисел.
Выводит на выбор: чётные/нечётные/простые числа.
'''
'''
Декоратор, замеряющий время работы функции, котороая определяет,
простое ли число:
'''
def my_timer(f):
    @functools.wraps(f)
    def tmp(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        delta_time = time.time() - start_time
        print('Время выполнения функции {}'.format(delta_time))
        return result

    return tmp
'''
Функция для определения, простое ли число
'''
@my_timer
def is_prime(num=3):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, math.trunc(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    else:
        return True


# Фильтрация чисел
def filtration(numbers=[1], num_type=1):
    answer = []
    if num_type == TYPE_EVEN:
        answer = list(filter(lambda x: x % 2 == 0, numbers))
        if answer == [] :
            print('There are no any even numbers in the list!')
        else:
            print('Even numbers in the list:')
            print(answer)
    elif num_type == TYPE_ODD:
        answer = list(filter(lambda x: x % 2 != 0, numbers))
        if answer == [] :
            print('There are no any odd numbers in the list!')
        else:
            print('Odd numbers in the list:')
            print(answer)
    elif num_type == TYPE_PRIME:
        answer = list(filter(is_prime, numbers))
        if answer == [] :
            print('There are no any primes in the list!')
        else:
            print('Primes in the list:')
            print(answer)
    else:
        print('Wrong constant!')
    return answer

'''Функция №3: вычисление чисел Фибоначчи с рекурсией'''
'''
Декоратор trace определяет вложенные входы в функцию
'''
def trace(func):
    func.level = 0
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('____' * func.level + ' --> {}({})'.format(func.__name__, args[0]))
        func.level += 1
        f = func(*args, **kwargs)
        func.level -= 1
        print('____' * func.level + ' <-- {}({}) == {}'.format(func.__name__, args[0], f))
        return f
    return inner

@trace
def fibonacci(n):
    """Считает числа Фибоначчи с рекурсией"""
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print('Home work No 1')

# Задаём исходный список из N чисел (nums_initial)
# Пусть этот список состоит из множества
# случайных целых чисел от 1 до 1000
print('Function "Exponentiation"')
print('')
nums_initial = []
N = 10

for i in range(1, N):
    nums_initial.append(random.randint(1, 1000))
print('Initial list of numbers:')
print(nums_initial)

# пример работы функции возведения в степень m чисел из списка
print()
m = 4
print('Exponentiation. Exponent is', m)
print('')
print('Result:')
print(my_pow_map(nums_initial, m))


# Пример работы функции фильтрации чисел.
# Сгенерируем список из N случайных целых чисел в диапазоне от 1 до 1000
print('Function "Filter"')
print('')
N = 5
nums_initial = []
for i in range(N):
    nums_initial.append(random.randint(1, 1000))
print('Initial list of numbers:')
print(nums_initial)

print('')
filtration(nums_initial, TYPE_EVEN)

filtration(nums_initial, TYPE_ODD)

filtration(nums_initial, TYPE_PRIME)

'''
Пример работы функции вычисления чисел Фибоначчи Quantity 
'''
print('')
print('Function 3: Fibonacci + @Trace')

Quantity = 5
print(Quantity, 'first Fibonacci numbers:')

for i in range(1, Quantity+1):
    fibonacci(i)

print('Check zero Fibonacci number:', fibonacci(0))

'''
Пример работы декоратора Trace

print('Trace')
'''



