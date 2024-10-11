from collections import deque

def solution(maps):
    
    rows, cols = len(maps), len(maps[0])
    
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    queue = deque([(0,0,1)])
    visited = set([(0,0)])
    
    while queue:
        x, y, distance = queue.popleft()
        
        if x == cols - 1 and y == rows -1:
            return distance
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < cols and 0 <= ny < rows and maps[ny][nx] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, distance + 1))
    return -1