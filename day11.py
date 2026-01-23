# Write a function that sorts an array of integers in ascending order using selection sort (no built-in sort).
# Requirements
# 	•	Concept:
# 	•	Treat the array as sorted part (left) + unsorted part (right).
# 	•	For each position `i`, find the smallest element in the unsorted part and swap it with position `i`.
# 	•	Use:
# 	•	An outer loop over indices `i` from start to end.
#   •	An inner loop to find the index of the minimum element from `i` to the end.
#   •	Swap only once per outer loop (after you know the min index).

array = [5, 7, 14, 1, 12, 3]


def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

print(selection_sort(array))
