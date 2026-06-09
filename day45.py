# depth first search (DFS) implementation using stack

class Stack :
    def __init__(self) :
        self.stack = []

    def push(self, item) :
        self.stack.append(item)

    def pop(self) :
        if not self.is_empty() :
            return self.stack.pop()
        else :
            raise IndexError("Stack is empty")

    def peek(self) :
        if not self.is_empty() :
            return self.stack[-1]
        else :
            raise IndexError("Stack is empty")

    def is_empty(self) :
        return len(self.stack) == 0

    def size(self) :
        return len(self.stack)
    

def dfs(graph, start) :
    visited = set()
    stack = Stack()
    stack.push(start)

    while not stack.is_empty() :
        vertex = stack.pop()

        if vertex not in visited :
            print(vertex)
            visited.add(vertex)

            for neighbor in graph[vertex] :
                if neighbor not in visited :
                    stack.push(neighbor)


def bfs(graph, start) :
    visited = set()
    queue = []
    queue.append(start)

    while queue :
        vertex = queue.pop(0)

        if vertex not in visited :
            print(vertex)
            visited.add(vertex)

            for neighbor in graph[vertex] :
                if neighbor not in visited :
                    queue.append(neighbor)







# Example usage
if __name__ == "__main__" :
    # Create a 4x4 grid with letters a-p
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

    # Create the 4x4 grid
    grid = []
    for row in range(4):
        grid_row = letters[row * 4: (row + 1) * 4]
        grid.append(grid_row)

    # Print the grid
    print("4x4 Grid:")
    for row in grid:        
        print(" ".join(row))

    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'F'],
        'C': ['G', 'H'],
        'D': ['I', 'J'],
        'E': [],
        'F': ['K', 'L'],
        'G': [],
        'H': [],
        'I': [],
        'J': ['M', 'N'],
        'K': [],
        'L': [],
        'M': [],
        'N': [],
    }

    print("Depth First Search (DFS):")
    dfs(graph, 'A')

    print("\nBreadth First Search (BFS):")
    bfs(graph, 'A')


