from collections import deque

y, x = map(int, input().split())

maps = [list(input().strip()) for _ in range(y)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start_y, start_x):
    visited = [[-1] * x for _ in range(y)]
    queue = deque([(start_y, start_x)])
    visited[start_y][start_x] = 0  # 시작 위치의 거리를 0으로 설정

    max_distance = 0
    
    while queue:
        current_y, current_x = queue.popleft()

        for dy, dx in directions:
            ny, nx = current_y + dy, current_x + dx
            
            # 범위 내에 있고, 육지이며, 아직 방문하지 않은 경우
            if 0 <= ny < y and 0 <= nx < x and maps[ny][nx] == 'L' and visited[ny][nx] == -1:
                visited[ny][nx] = visited[current_y][current_x] + 1
                max_distance = max(max_distance, visited[ny][nx])
                queue.append((ny, nx))
                
    return max_distance

max_distance = 0

# 모든 육지에서 BFS를 수행하여 최대 거리 찾기
for i in range(y):
    for j in range(x):
        if maps[i][j] == 'L':
            max_distance = max(max_distance, bfs(i, j))

print(max_distance)
