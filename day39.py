#Challenge: “Two‑Sum with Closest Pair”
#Given a list of integers  nums  and a target value  target , 
# find two numbers in the list whose sum is closest to the target 
# (but not necessarily equal to it). Return the pair of values and the
# absolute difference between their sum and the target.

numbers = [1, 3, 9, 4, 7, 2]
target  = 8


def find_two_sum_closest_pair(numbers, target):
    if len(numbers) < 2:
        return None

    best_pair = (numbers[0], numbers[1])
    best_diff = abs(numbers[0] + numbers[1] - target)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            a, b = numbers[i], numbers[j]
            curr_sum = a + b
            curr_diff = abs(curr_sum - target)

            if curr_diff < best_diff:
                best_diff = curr_diff
                best_pair = (a, b)

    return best_pair, best_diff
        
print(find_two_sum_closest_pair(numbers, target))

