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

# Example usage
if __name__ == "__main__" :
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("Depth First Search starting from vertex A:")
    dfs(graph, 'A')


