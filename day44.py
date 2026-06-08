#anagram check

from collections import Counter 

def check_if_anagram(a, b):
    # true_count = 0
    # if len(a) != len(b):
    #     return False
    # else:
    #     for letter in a:
    #         if letter in b:
    #             true_count += 1
    #         else:
    #             return False
    #     if true_count == len(a):
    #         return True

    return Counter(a) == Counter(b)
        

a = "rat"
b = "tar"


print(check_if_anagram(a, b))