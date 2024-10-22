from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
  graph.append(list(map(int, input())))

def bfs(start):

  queue = deque([(*start, 1)])
  visited = [[False] * m for _ in range(n)]
  visited[start[0]][start[1]] = True 
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  
  while queue:
    y, x, dis = queue.popleft()
    if (y, x) == (n - 1, m - 1):
      print(dis)
      return dis

    for dy, dx in directions:
      ny, nx = dy + y, dx + x

      if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == False and graph[ny][nx] == 1:
        visited[ny][nx] = True
        queue.append((ny, nx, dis + 1))
  return -1

bfs((0, 0))