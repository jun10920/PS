import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한을 늘리기

def dfs(y, x):

  maps[y][x] = 0

  for dy, dx in directions:
    ny, nx = y + dy, x + dx

    if 0 <= ny < h and 0 <= nx < w and maps[ny][nx] == 1:
      dfs(ny, nx)  

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
answerList = []

while True:
  w, h = map(int, input().split())

  if (w, h) == (0, 0):
    break

  maps = []
  for _ in range(h):
    maps.append(list(map(int, input().split())))

  temp = 0
  
  for i in range(h):
    for j in range(w):
      if maps[i][j] == 1:
        dfs(i, j)
        temp += 1

  answerList.append(temp)

for i in answerList:
  print(i)