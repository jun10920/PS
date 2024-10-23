from collections import deque

n, k = map(int, input().split())

def bfs(start, end):
    if start == end:
        return 0
    
    visited = [False] * 100001  # 배열 크기를 100001로 설정
    visited[start] = True
    count = 0
    queue = deque([(start, count)])

    while queue:
        current, count = queue.popleft()

        for next in (current + 1, current - 1, current * 2):
            if 0 <= next <= 100000 and not visited[next]:  # 범위를 0 <= next <= 100000으로 수정
                if next == end:
                    return count + 1
                queue.append((next, count + 1))
                visited[next] = True  # 방문 체크를 잊지 않도록 추가

print(bfs(n, k))