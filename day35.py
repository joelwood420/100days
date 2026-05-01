def first_not_repeating_character(string):
    counts = {}
    for s in string:
        counts[s] = counts.get(s, 0) +1

    for t in string:
        if counts[t.py6] == 1:
            return t






print(first_not_repeating_character("swiss"))

        
        