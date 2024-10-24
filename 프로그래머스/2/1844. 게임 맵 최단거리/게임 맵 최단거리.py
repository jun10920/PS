from collections import deque
def solution(maps):
    
    rows , cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[0][0] = True
    
    def bfs():
        queue = deque([(0,0,1)])
        while queue:
            y, x, dis = queue.popleft()
            
            if (y, x) == (rows - 1, cols - 1):
                return dis
            for dy, dx in directions:
                ny, nx = dy + y, dx + x

                if 0 <= ny < rows and 0 <= nx < cols and not visited[ny][nx] and maps[ny][nx] != 0:
                    visited[ny][nx] = True
                    queue.append((ny, nx, dis + 1))
        return -1
    return bfs()