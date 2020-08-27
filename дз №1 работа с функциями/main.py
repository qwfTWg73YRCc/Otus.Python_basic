
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

def my_pow(numbers=[1, 2], expo=2):
    for i in range(len(numbers)):
        numbers[i] = operator.pow(numbers[i], expo)
    return numbers

def plus_1(numbers=[1, 2]):
    for i in range(len(numbers)):
        numbers[i] += 1
    return numbers

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
nums_initial = []
N = 10

for i in range(1, N):
    nums_initial.append(random.randint(1, 1000))
print('Initial list of numbers:')
print(nums_initial)

# тестирование возведения в степень списка

a = [1, 2, 3]
print(plus_1(a))
print(my_pow(nums_initial))
for i in range(len(a)):
    a[i] += 1

print(a)

# Список чисел, возведённых в степень
exp = []

# Выполнение функции возведения в степень.

# exp = my_pow(nums_initial, 2)

# print(my_pow(nums_initial, 2))
# print(plus_1(nums_initial, 2))

# print(exp)
# print(nums_initial[i])


'''
for i in range(r):
    print("Введите", i+1, "число:")
    b.append(input("число: "))
    exp.append(exponent_num)
    while not b[i].isdigit():
        print('Это не число!')
        print("Введите", i+1, "число")
        b.append(input("число: "))
    b[i] = float(b[i])
'''
# Конечно, проще так, но тогда не понятно, как писать
# условие на корректность ввода
# b = [float(input('Число : ')) for i in range(r)]


# print('Вы ввели: ', b)

# функция возведения в степень power


# def power(a=1, expo=2):
#    operator.pow(a, expo)

# возведение в степень с помощью map и operator.pow


# exponentiated = list(map(operator.pow, b, exp))
# print("Возведение в степень:", exponentiated)


from pprint import pprint
N = input('Количество чисел: ')

if N.isdigit():
    N = int(N)
else:
    N = ''
    print('error')
    N = input('Количество чисел: ')

a = [i for i in range(N)]

print(a)


choose = input('Вывести: четные (1), нечётные (2), простые (3) :')


# замеряет время на проверку, является ли заданное число простым
# для каждого числа из списка

def my_timer(f):
    @functools.wraps(f)
    def tmp(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        delta_time = time.time() - start_time
        print('Время выполнения функции {}'.format(delta_time))
        return result

    return tmp


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





