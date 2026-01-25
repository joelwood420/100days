string = 'hdytdbjwakjsowqjcvanmZoroyqp'

def count_vowels(s):
    vowels = 'aeiou'
    counter = 0
    for char in s:
        if char in vowels:
            counter += 1
    return counter
print(count_vowels(string))


