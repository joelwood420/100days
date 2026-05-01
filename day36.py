def two_sum_pairs(nums, target):
    pairs = []
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            pairs.append([num_to_index[complement], i])
        num_to_index[num] = i

    return pairs
  

# Test
print(two_sum_pairs([2,7,11,15], 9))  # [[0,1]]