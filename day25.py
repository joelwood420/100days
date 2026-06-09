# Build a tiny “functional filter engine” for lists of numbers.
# Challenge: Functional Filter Engine
# Write a function  build_filter(predicates)  that:
# 	•search algorithmas	Takes a list of predicate functions  predicates , where each predicate is a  func(x) -> bool .
# 	•	Returns a new function  filter_numbers(numbers)  that:
# 	•	Takes a list of integers  numbers .
# 	•	Returns a new list containing only the numbers that satisfy all predicates.
# You must use higher-order functions (functions that take/return functions) and avoid writing explicit  for  loops in  filter_numbers  (use  filter ,  map , or comprehensions instead).




def create_filter(pred_1):
    if pred_1 == "even":
        return lambda x: x % 2 == 0
    elif pred_1 == "odd":
        return lambda x: x % 2 != 0
    elif pred_1.startswith("greater_than_"):
        threshold = int(pred_1.split("_")[-1])
        return lambda x: x > threshold
    elif pred_1.startswith("less_than_"):
        threshold = int(pred_1.split("_")[-1])
        return lambda x: x < threshold
    else:
        raise ValueError(f"Unknown predicate: {pred_1}")


even_filter = create_filter("even")
odd_filter = create_filter("odd")
greater_than_5_filter = create_filter("greater_than_5")
less_than_10_filter = create_filter("less_than_10")


numbers = [-3, -2, -1, 0, 1, 2, 3, 4]

print(list(filter(even_filter, numbers)))
print(list(filter(odd_filter, numbers)))
print(list(filter(greater_than_5_filter, numbers)))
print(list(filter(less_than_10_filter, numbers)))