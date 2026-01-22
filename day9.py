# Two Sum. Given a list of integers `nums` and a target integer `target`, 
# return indices of two numbers that add up to `target`. Assume exactly one solution,
# no same element use twice.

nums = [2, 7, 11, 15]

target = 9


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        print(num, )
        print(i)
        needed = target - num
        print('needed: ', needed)
        if needed in seen:
            print(seen)
            return [seen[needed], i]
        seen[num] = i 
    return [ ]



print(two_sum(nums, target))





