from collections import deque
n, k = map(int ,input().split())
visited = [False] * 100001


def bfs(n, k):
    queue = deque([(n, 0)])

    while queue:
        current_pos, count = queue.popleft()
        if current_pos == k:
            return count
        for i in (current_pos - 1, current_pos + 1, current_pos  * 2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = True
                queue.append((i, count + 1))
    return count
print(bfs(n, k))