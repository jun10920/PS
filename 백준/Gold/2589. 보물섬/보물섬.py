from collections import deque

h, w = map(int, input().split())
maps = [input() for _ in range(h)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(start_y, start_x):
    queue = deque([(start_y, start_x, 0)])
    visited = [[False] * w for _ in range(h)]
    visited[start_y][start_x] = True
    max_dis = 0

    while queue:
        y, x, dis = queue.popleft()
        max_dis = max(max_dis, dis)
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and maps[ny][nx] != 'W' and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, dis + 1))
    return max_dis

answer = float('-inf')
for i in range(h):
    for j in range(w):
        if maps[i][j] != 'W':
            answer = max(answer, bfs(i, j))
print(answer)