# Write a function  make_counter()  that returns a “counter function.” 
# Each call to the counter increments and returns the next integer, starting from 1.
#  Closures make this perfect functional style.


def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter


counter = make_counter()
increment = counter

print(counter())

increment()
increment()
print(counter())