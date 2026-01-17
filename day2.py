# challenge 2
# Reverse a String. Write a function that takes a string as 
# input and returns it reversed. For example, “hello” becomes “olleh”.



# First attempt

def reverse_string(text):
    for i in reversed(text):
        print(i, end='')
    

# reverse_string('hello')

strings = [
    'hello',
    'python',
    'joel',
    'racecar'
]


for string in strings:
    reverse_string(string)


# Refactor

def reverse_string(text):
    # Slicing [startpoint:endpoint:step]
    return text[::-1]

for string in strings:
    print(reverse_string(string))