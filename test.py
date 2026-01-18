class stack:
    def __init__(self):
        self.item = []

    def pop(self):
        return self.item.pop()
    
    def push(self, item):
        return self.item.append(item)

string = 'my name is joel'

s = stack()
for char in string:
    s.push(char)

reversed_string = ''

while s.item:
    reversed_string += s.pop()

print(reversed_string)
    
    
    


