# math module functions demonstration
import math
print(math.copysign(3, -2))
print(math.fabs(-7.5))
print(math.factorial(5))
print(math.isqrt(16))
print(math.sqrt(49))
print(math.gcd(48, 18))
print(math.lcm(4, 6))
print(math.ceil(4.3))


def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print(multiply([1, 2, 3, 4, 5]))
