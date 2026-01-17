# Fibonacci Sequence. Write a function that returns the nth Fibonacci number (non-recursive, iterative). 
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13…


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        next = a + b
        a = b
        b = next
    return a


print(fibonacci(3))