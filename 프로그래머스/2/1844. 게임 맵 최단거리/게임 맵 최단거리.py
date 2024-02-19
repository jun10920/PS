from collections import deque

def bfs(maps, x, y, n, m):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]  # 수정된 부분
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1  # 수정된 부분

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    return bfs(maps, 0, 0, n, m)
