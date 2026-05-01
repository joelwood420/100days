# Write a function that takes a list of integers and returns a new 
# list where each element is the product of all the other elements except 
# the one at that index. This is a classic interview problem and a 
# strong test of array handling and optimization


numbers=[1, 5, 9, 7, 6]

def product_of(numbers):
    index = 0
    new_list =[]
    for num in numbers:
        num = numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4]
        product = num // numbers[index]
        index += 1
        new_list.append(product)

    return new_list


print(product_of(numbers))
        
