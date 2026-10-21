import math
from sympy import factorint, primerange, isprime

def is_prime(n: int) -> bool:
    if n < 2: 
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            
    return True

def task6_prime_factors(n: int) -> list[int]:
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def task8_primes_up_to(N: int) -> list[int]:
    return list(primerange(2, N + 1))

def task13_prime_digit_sum_in_range(a: int, b: int) -> list[int]:
    res = []
    for prime in primerange(max(2, a), b + 1):
        digit_sum = sum(int(digit) for digit in str(prime))
        if isprime(digit_sum):
            res.append(prime)
            
    return res

if __name__ == "__lab2__":
    print("Задание 6: Множители числа 315:")
    print(task6_prime_factors(315))
    
    print("\nЗадание 8: Простые числа до 50:")
    print(task8_primes_up_to(50))
    
    print("\nЗадание 13: Простые с простой суммой цифр [10, 150]:")
    print(task13_prime_digit_sum_in_range(10, 150))