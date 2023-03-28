import math
from datetime import datetime
import datetime
x= 100000
number = 2000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001


def timer(func):
    def wrapped(*args, **kwargs):
        start = datetime.datetime.now()
        answer = func(*args, **kwargs)
        res_time = datetime.datetime.now() - start
        print(res_time)
        return answer
    return wrapped


@timer
def find_smallest_multiple(number):
    if number < 1:
        raise ValueError("Number must be a positive integer greater than zero.")
    for i in range(2, number + 1, 2):
        if math.gcd(i, number) == 2:
            return i


@timer
def tru_method(number):
    if number % 2 == 0:
        return number
    else:
        return 2 * number


@timer
def brut(number):
    counter = 2
    while True:
        if counter % 2 == 0:
            if counter % number == 0:
                break
        counter += 2
    return counter


@timer
def brutella(number):
    for i in range(x)*z
    for i in range(0, 2*number + 1, number):
        if i % 2 == 0 and i != 0:
            return i


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


@timer
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


print(lcm(2, number))
print(brutella(number))
print(tru_method(number))
