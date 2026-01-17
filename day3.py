# Day 3 Challenge
# Find Largest Number in Array. Write a function that takes an array of numbers and returns the largest one
# Do not use built-in max functions.

def largest_number(array):
    largest = None
    for number in array:
        if largest == None or number > largest:
            largest = number
    return largest



numbers = [-1, -3, -9, -7, -3, -4, -8, -3]

print(largest_number(numbers))


#Quick Feedback
	# Clean iteration and comparison.
	# Edge cases like empty arrays could add `if not array: return None`, but your tests work great.
	# Efficient single pass (O(n) time).



# AI Solution 


def largest_number(array):
    if not array:
        return None
    largest = array[0]  # Start with first element
    for number in array[1:]:
        if number > largest:
            largest = number
    return largest