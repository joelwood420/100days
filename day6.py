 # Factorial of n. 
 # Write a recursive function to compute n! (n factorial: product of all positive integers up to n). 


def factorial(n):
    if n == 0:
       return 1
    else :
        return n * factorial(n-1) # each time n is multiplyed by n-1 until n = 0


print(factorial(5))