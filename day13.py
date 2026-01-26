# Write a function that returns `True` if a number is prime, `False` otherwise.
# Prime = number > 1 with no divisors other than 1 and itself.
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(sqrt(n)+2)))
         

print(is_prime(4))
    


