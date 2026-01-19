# Write a function that implements binary search on a sorted list of integers and returns the index of the target if found, or `-1` if not found.
# Requirements
# 	•	Input: a sorted list `nums` and an integer `target`.
# 	•	Output: the index of `target` in `nums`, or `-1` if it is not present.
# 	•	Use the iterative approach with `low`, `high`, and `mid` pointers.
# 	•	Do not use built-in search methods.
# Test cases to try
# 	•	`nums = , target = 7` → `3`
# 	•	`nums = , target = 2` → `-1`
# 	•	`nums = [], target = 10` → `-1`
# 	# •	`nums = , target = 4` → `0`



nums = [1,2,3,4,5,6,7,8,9]

target = 7

def binary_search(nums, target):
    low = 0 
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2        #find the mid point of the array
        if nums[mid] == target:              #check if midpoint is the target 
            return mid                       #returns the index of the target
        elif nums[mid] < target:             #otherwise if the target is higher than the mid point
            low = mid + 1                    #add one to the middle index and assign it to the new low(floor)
        else:                                #if the target is lower
            high = mid - 1                   #minus one from the mid point and this will be the new high
                                             #iterate over agian searching between the the new high and low,



                                             #binary search essentially goes to the middle
                                             #checks if its left or right 
                                             #does the same agiain till target is found
                                             # essentially halfing the problem, halfing it again till target is found 








print(binary_search(nums, target))

