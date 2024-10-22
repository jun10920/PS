n = int(input())

maps = [list(map(int, input())) for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(y, x):
  count = 1
  maps[y][x] = 0

  for dx, dy in directions:
    ny, nx = y + dy, x + dx
    if 0 <= ny < n and 0 <= nx < n and maps[ny][nx] != 0:
      count += dfs(ny, nx)
  return count

apts = []

for i in range(n):
  for j in range(n):
    if maps[i][j] !=0:
      apts.append(dfs(i, j))

apts.sort()
print(len(apts))

for i in apts:
  print(i)