def get_prime_numbers(numbers):
    primes = []
    for i in numbers:
        if is_prime(i):
            primes.append(i)
    return primes







def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 4, 5, 6, 7, 9, 11]

print(get_prime_numbers(numbers))