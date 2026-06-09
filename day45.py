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


def find_in_grid(grid, target):
    """Find the position of a target value in the grid"""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == target:
                return (row, col)
    return None


def find_path_bfs(grid, start, end):
    """BFS to find shortest path from start to end in a 2D grid"""
    start_pos = find_in_grid(grid, start)
    end_pos = find_in_grid(grid, end)
    
    if not start_pos or not end_pos:
        return None
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = [(start_pos, [start_pos])]  # (position, path)
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        (row, col), path = queue.pop(0)
        
        if (row, col) == end_pos:
            return path
        
        if (row, col) in visited:
            continue
        
        visited.add((row, col))
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (new_row, new_col) not in visited):
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))
    
    return None


def find_path_dfs(grid, start, end):
    """DFS to find path from start to end in a 2D grid"""
    start_pos = find_in_grid(grid, start)
    end_pos = find_in_grid(grid, end)
    
    if not start_pos or not end_pos:
        return None
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    stack = [(start_pos, [start_pos])]  # (position, path)
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while stack:
        (row, col), path = stack.pop()
        
        if (row, col) == end_pos:
            return path
        
        if (row, col) in visited:
            continue
        
        visited.add((row, col))
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (new_row, new_col) not in visited):
                stack.append(((new_row, new_col), path + [(new_row, new_col)]))
    
    return None







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

    # DFS Search
    print("Finding path from 'a' to 'p' in grid (DFS):")
    path_dfs = find_path_dfs(grid, 'a', 'p')
    
    if path_dfs:
        print(f"Path found! Length: {len(path_dfs)} steps")
        print("Path coordinates (row, col):")
        for i, (row, col) in enumerate(path_dfs):
            print(f"  Step {i}: ({row}, {col}) -> '{grid[row][col]}'")
    else:
        print("No path found!")

    # BFS Search
    print("\n\nFinding path from 'a' to 'p' in grid (BFS):")
    path_bfs = find_path_bfs(grid, 'a', 'p')
    
    if path_bfs:
        print(f"Path found! Length: {len(path_bfs)} steps")
        print("Path coordinates (row, col):")
        for i, (row, col) in enumerate(path_bfs):
            print(f"  Step {i}: ({row}, {col}) -> '{grid[row][col]}'")
    else:
        print("No path found!")


