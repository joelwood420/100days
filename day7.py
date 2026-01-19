# Sum Array Recursively. Write a recursive function that returns the sum of all numbers in an array.
#  Base case: empty array sums to 0.




numbers = [1, 2, 3, 4, 5]

def sum_array(n):
    if not n:
        return 0
    else:
        return n[0] + sum_array(n[1:])
   


print(sum_array(numbers))
    