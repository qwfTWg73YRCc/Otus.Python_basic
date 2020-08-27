
import operator
import math
import time
import functools
import random


if __name__ == '__main__':
    print('Home work No 1')

'''
Функция №1.
Принимает список из N целых чисел 
и выдаёт список из них возведённых в заданную степень
'''
i = 0

def my_pow_map(numbers=[1, 2], expo=2):
    expon = []
    for i in range(len(numbers)):
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
def filtration(numbers=[1, 2], CONSTANT = 1):
    answer = []
    if CONSTANT == 1:
        answer = list(filter(lambda x: x % 2 == 0, numbers))
        print('Even numbers in the list:')
        print(answer)
        if answer == [] :
            print('There are no any odd numbers in the list!')
    elif CONSTANT == 2:
        answer = list(filter(lambda x: x % 2 != 0, numbers))
        print('Odd numbers in the list:')
        print(answer)
        if answer == [] :
            print('There are no any odd numbers in the list!')
    elif CONSTANT == 3:
        answer = list(filter(is_prime, numbers))
        print('Primes in the list:')
        print(answer)
        if answer == [] :
            print('There are no any primes in the list!')
    return answer

'''Функция №3: вычисление чисел Фибоначчи с рекурсией'''

'''
Декоратор trace определяет вложенные входы в функцию
'''

def fibonacci(n):
    """Считает числа Фибоначчи с рекурсией"""
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)



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
m = 5
print('Exponentiation:', m, 'power')
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
filtration(nums_initial, 1)
filtration(nums_initial, 2)
filtration(nums_initial, 3)

'''
Пример работы функции вычисления Quantity чисел Фибоначчи
'''
print('')
print('Function 3: Fibonacci + @Trace')

Quantity = 5
print(Quantity, 'first Fibonacci numbers:')

for i in range(1, Quantity+1):
    print(fibonacci(i))

'''
Пример работы декоратора Trace
'''
print('Trace')




