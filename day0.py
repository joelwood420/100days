from dataclasses import dataclass




def type_of(a, b, c):
    if a == b and b == c: return 'equalateral'
    elif a == b or b == c: return 'isosalese'
    else : return 'scalene'

print(type_of(5, 4, 9))


# initalizing a new data type of triangle 
@dataclass
class Triangle:
    a: int
    b: int
    c: int
    
    
    
triangles = [
    Triangle(3, 5, 9),
    Triangle(6, 6, 6),
    Triangle(7, 2, 2),
    Triangle(1, 5, 5),
    Triangle(3, 7, 1)
]

def calculate_perimeter(a, b, c):
    perimeter = a + b + c
    return perimeter

smallest = None
smallest_perimeter = None


for t in triangles:
    if type_of(t.a, t.b, t.c) == 'scalene':
        p = calculate_perimeter(t.a, t.b, t.c)
        if smallest is None or p < smallest_perimeter:
            smallest = t
            smallest_perimeter = p


print(smallest)

      
        
