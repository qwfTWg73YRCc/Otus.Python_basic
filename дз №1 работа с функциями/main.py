
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
'''
def my_pow(numbers=[1, 2], expo=2):
    for i in range(len(numbers)):
        numbers[i] = operator.pow(numbers[i], expo)
    return numbers
'''
def my_pow_map(numbers=[1, 2], expo=2):
    expon = []
    for i in range(len(numbers)):
        expon.append(expo)
    return list(map(operator.pow, numbers, expon))


'''
Функция №2: принимает на вход список из целых чисел.
Выводит на выбор: чётные/нечётные/простые числа.
'''
'''Декоратор, замеряющйи время работы функции, определяющей,
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
Отдельная функция для определения, простое ли число
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
'''
if choose == '1':
    even = list(filter(lambda x: x % 2 == 0, a))
    print(even)
elif choose == '2':
    odd = list(filter(lambda x: x % 2 != 0, a))
    print(odd)
elif choose == '3':
    primes = list(filter(is_prime, a))
    if not primes:
        print('В списке нет простых чисел!')
    else:
        print(primes)
'''

'''    
     = input('Введите число чисел: ')
    exponent = input('Введите показатель степени: ')


while not ran.isdigit() or not exponent.isdigit():
    print('error')
    if not ran.isdigit():
        ran = input('Введите число чисел: ')
    if not exponent.isdigit():
        exponent = input('Введите показатель степени: ')

exponent_num = int(exponent)
r = int(ran)
# exponent must be an integer

# r must be a positive integer

# b[i] must be an integer
'''
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

'''
N = input('Количество чисел: ')

if N.isdigit():
    N = int(N)
else:
    N = ''
    print('error')
    N = input('Количество чисел: ')

a = [i for i in range(N)]

print(a)
'''

# choose = input('Вывести: четные (1), нечётные (2), простые (3) :')

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
if choose == '1':
    even = list(filter(lambda x: x % 2 == 0, a))
    print(even)
elif choose == '2':
    odd = list(filter(lambda x: x % 2 != 0, a))
    print(odd)
elif choose == '3':
    primes = list(filter(is_prime, a))
    if not primes:
        print('В списке нет простых чисел!')
    else:
        print(primes)
'''
qua = int(input('Введите количество чисел Фибоначчи: '))


def fibonacci(n):
    """Считает числа Фибоначчи с рекурсией"""
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, qua+1):
    print(fibonacci(i))
"По поводу подсчёта входов я ничего не понял,"
"но хотел бы увидеть решение. Интересно."





