class stack:
    def __init__ (self):
        self.item = []

    def pop(self):
        return self.item.pop()
    
    def push(self, item):
        return self.item.append(item)
    

def is_valid(string):
    s = stack()
    for char in string:
        if char in '([{':
            s.push(char)
        else:
            if not s.item:
                return False
            top = s.pop()
            if char == ')' and top != '(':
                return False
            elif char == ']' and top != '[':
                return False
            elif char == '}' and top != '{':
                return False
    return not s.item


print(is_valid('()'))         
