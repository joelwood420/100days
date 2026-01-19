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


# using slicing 

def reverse_string(text):
    # Slicing [startpoint:endpoint:step]
    return text[::-1]

for string in strings:
    print(reverse_string(string))


# using a Stack to reverse a string 

class stack:
    def __init__(self):
        self.item = []

    def pop(self):
        return self.item.pop()      # creating methods 
    
    def push(self, item):
        return self.item.append(item)

string = 'my name is joel'

s = stack()         # loop through pushing each character onto the stack
for char in string:
    s.push(char)

reversed_string = ''     

while s.item:         # poping each character off the top one by one and saving it into reverse string
    reversed_string += s.pop()

print(reversed_string)