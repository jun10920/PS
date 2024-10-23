from collections import deque
n, k = map(int, input().split())

answer = float('inf')

def bfs(start, target):
  if start == target:
      return 0

  queue = deque([(start, 0)])  # (현재 위치, 이동 횟수)
  visited = [False] * 100001  # 방문 체크 배열 (문제 조건에 따라 범위 설정)
  visited[start] = True

  while queue:
      current, count = queue.popleft()

      # 가능한 이동 (현재 위치 +1, -1, *2)
      for next_position in (current + 1, current - 1, current * 2):
          if 0 <= next_position <= 100000 and not visited[next_position]:
              if next_position == target:
                  return count + 1
              queue.append((next_position, count + 1))
              visited[next_position] = True

# BFS 실행
print(bfs(n, k))