string = 'feEAt'

# def count_vowels(s):
#     vowels = 'aeiou'
#     counter = 0
#     s = s.lower()
#     for char in s:
#         if char in vowels:
#             counter += 1
#     return counter
        
# print(count_vowels(string))



def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

print(count_vowels(string))









    